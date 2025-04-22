@echo off
java -Xmx500M -cp antlr-4.13.0-complete.jar;%CLASSPATH% org.antlr.v4.Tool %*
