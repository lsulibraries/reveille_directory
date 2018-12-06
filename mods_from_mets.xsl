<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet 
    xmlns="http://www.loc.gov/mods/v3"
    xmlns:MODS="http://www.loc.gov/mods/v3"
    xmlns:mods="http://www.loc.gov/mods/v3"
    xmlns:mets="http://www.loc.gov/METS/"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:mix="http://www.loc.gov/mix/"
    exclude-result-prefixes="mix mets" 
    version="2.0" >
    
    <!--
        A stylesheet for extracting MODS from METS documents and adding LDL boilerplate metadata, 
        adhering to LDL MODS default guidance.
        
        This was built for the LSU Reveille newspaper project with vendor-supplied METS records,
        and specific field values are set accordingly.
    -->
    <xsl:output method="xml" indent="yes" encoding="UTF-8" />
    
    <!-- Get the publication / volume metadata from the MODSMD_ELEC section -->
    <xsl:variable name="pubMeta" select="//mets:dmdSec[contains(@ID,'MODSMD_ELEC')]//MODS:mods"/>
    <xsl:variable name="dateCaptured">
        <xsl:variable name="datePart" select="tokenize($pubMeta//MODS:dateCreated, '\.')"/>
        <xsl:value-of select="concat($datePart[3], '-', $datePart[2], '-', $datePart[1])"/>
    </xsl:variable> 
    <xsl:variable name="publisher" select="$pubMeta//MODS:publisher"/>
    <xsl:variable name="pubTitle" select="$pubMeta//MODS:title"/>
    <xsl:variable name="volume" select="$pubMeta//MODS:partNumber"/>
    <xsl:variable name="volumeID" select="$pubMeta//MODS:identifier"/>
        
    <!-- Set up transform pointing to the issue metadata -->
    <xsl:template match="mets:mets">
        <xsl:apply-templates select="//mets:dmdSec[contains(@ID,'MODSMD_ISSUE')]//MODS:mods"/>
    </xsl:template>
    
    <!-- Identity transform; normalize space and strip empty nodes -->
    <xsl:template match="@* | node() ">
        <xsl:copy>
            <xsl:apply-templates select="@*[normalize-space()] | node()[normalize-space()] "/>
        </xsl:copy>
    </xsl:template>
    
    <!-- Main template to build LDL issue-level MODS -->
    <xsl:template match="MODS:mods">
        <mods 
            xmlns="http://www.loc.gov/mods/v3"
            xmlns:mods="http://www.loc.gov/mods/v3"
            xmlns:xs="http://www.w3.org/2001/XMLSchema"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd"
            version="3.5" 
            >
            <titleInfo>
                <nonSort>The</nonSort>
                <title>
                    <xsl:text>Daily Reveille, Vol. </xsl:text>
                    <xsl:value-of select="$volume"/>
                    <xsl:text> No. </xsl:text>
                    <xsl:value-of select="MODS:titleInfo/MODS:partNumber"/>
                </title>
            </titleInfo>
            <titleInfo type="alternative">
                <title>Reveille</title>
            </titleInfo>
            <part>
                <detail type="volume">
                    <caption>Vol.</caption>
                    <number>
                        <xsl:value-of select="$volume"/>
                    </number>
                </detail>
                <detail type="issue">
                    <caption>No.</caption>
                    <number>
                        <xsl:value-of select="MODS:titleInfo/MODS:partNumber"/>
                    </number>
                </detail>
            </part>
            <xsl:if test="$volumeID != MODS:identifier">
                <identifier type="local">
                    <xsl:value-of select="MODS:identifier"/>
                </identifier>
            </xsl:if>
            <identifier type="local" displayLabel="Volume ID">
                <xsl:value-of select="$volumeID"/>
            </identifier>
            <identifier type="local" displayLabel="Item Number">
                <xsl:value-of select="concat('reveillecentennial_', replace(substring-after(base-uri(),'/reveillecentennial_'),'-METS.xml',''))"/>
            </identifier>
            <name type="corporate" authority="naf"
                authorityURI="http://id.loc.gov/authorities/names"
                valueURI="http://id.loc.gov/authorities/names/no2015036095"
                displayLabel="Contributing Repository">
                <namePart>LSU Libraries. Special Collections</namePart>
                <role>
                    <roleTerm type="text" authority="marcrelator"
                        authorityURI="http://id.loc.gov/vocabulary/relators"
                        valueURI="http://id.loc.gov/vocabulary/relators/rps">Repository</roleTerm>
                </role>
            </name>
            <name type="corporate" displayLabel="Digitized By">
                <namePart>
                    <xsl:value-of select="$publisher"/>
                </namePart>
                <role>
                    <roleTerm type="text"
                        authority="marcrelator"
                        authorityURI="http://id.loc.gov/vocabulary/relators"
                        valueURI="http://id.loc.gov/vocabulary/relators/fac">Facsimilist</roleTerm>
                </role>
            </name>
            <originInfo>
                <dateIssued keyDate="yes">
                    <xsl:value-of select="replace(MODS:originInfo/MODS:dateIssued,'\.','-')"/>
                </dateIssued>
                <dateCaptured>
                    <xsl:value-of select="$dateCaptured"/>
                </dateCaptured>
            </originInfo>
            <subject authority="lcsh">
                <topic>Louisiana State University (Baton Rouge, La.)</topic>
            </subject>  
            <typeOfResource>text</typeOfResource>
            <genre authority="aat">newspapers</genre>
            <physicalDescription>
                <form authority="aat">texts (documents)</form>
                <internetMediaType>image/jp2</internetMediaType>
                <digitalOrigin>reformatted digital</digitalOrigin>
            </physicalDescription>
            <language>
                <languageTerm type="code" authority="rfc3066">
                    <xsl:value-of select="MODS:language/MODS:languageTerm"/>
                </languageTerm>
                <xsl:if test="contains(MODS:language/MODS:languageTerm,'en')">
                    <languageTerm type="text">English</languageTerm>
                </xsl:if>
            </language>
            <relatedItem type="host">
                <titleInfo displayLabel="Digital Collection">
                    <title>The Daily Reveille</title>
                </titleInfo>
                <location>
                    <url displayLabel="Relation">http://louisianadigitallibrary.org/islandora/object/lsu-sc-reveille:collection</url>
                </location>
                <titleInfo type="alternative" displayLabel="Periodical Title">
                    <title>The Daily Reveille</title>
                </titleInfo>
            </relatedItem>
            <location>
                <physicalLocation displayLabel="Physical Location" xlink:href="http://lib.lsu.edu">LSU Libraries</physicalLocation>
                <physicalLocation authority="oclcorg" displayLabel="OCLC Member Symbol">LUU</physicalLocation>
            </location>
            <accessCondition xlink:href="http://rightsstatements.org/vocab/InC-NC/1.0/" type="use and reproduction" displayLabel="Rights Statement">In Copyright - Non-Commercial Use Permitted</accessCondition>\
            <accessCondition type="use and reproduction" displayLabel="Contact Information">Please submit an LSU Special Collections reference ticket at https://askus.lib.lsu.edu/special for any questions or comments about this digital object.</accessCondition>
            <recordInfo>
                <languageOfCataloging>
                    <languageTerm type="code" authority="iso639-2b">eng</languageTerm>
                </languageOfCataloging>
                <recordOrigin>METS from Backstage Library Works; MODS extracted and transformed using custom XSLT.</recordOrigin>
                <recordContentSource>lsu/cmk</recordContentSource>
                <recordCreationDate>
                    <xsl:value-of select="current-date()"/>
                </recordCreationDate>
            </recordInfo>
        </mods>
    </xsl:template>
    
</xsl:stylesheet>
