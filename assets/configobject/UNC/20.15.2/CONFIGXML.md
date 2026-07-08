---
id: UNC@20.15.2@ConfigObject@CONFIGXML
type: ConfigObject
name: CONFIGXML（XML文件配置到数据库）
nf: UNC
version: 20.15.2
object_name: CONFIGXML
object_kind: action
status: active
---

# CONFIGXML（XML文件配置到数据库）

## 说明

![](加载XML文件配置到数据库(LOD CONFIGXML)_49621485.assets/notice_3.0-zh-cn_2.png)

该命令为高危命令，执行时会导致CPU产生波动，如在业务高峰期需谨慎执行，且命令执行期间系统的操作维护类命令可能无法执行。请务必在华为技术支持人员的指导下使用该命令！

当在系统中批量执行配置类MML时，系统执行时间可能很长，为提升效率，可将配置MML命令写入XML格式的配置数据文件，将文件通过OM Portal上传至 “ 系统 > 文件传输 > 原子配置服务 ” 下，然后通过该命令将配置数据文件加载至ACS的数据库，再通过 **SYN ACSPEERCFG** 命令，将配置数据文件中的配置同步至各微服务。

该命令支持通过加载XML文件新增配置和删除配置，对应XML格式的配置数据文件格式如下所示。

- 新增配置：
  ```
  <?xml version="1.0" encoding="GBK"?>
  <db version="0.0.1">
      <data>
          <table name="
  testAssMain
  " version="1.0" reparse="false">
              <record 
  index
  =
  "1" ifName
  =
  "aa"
   />
          </table>
      </data>
  </db>
  ```

- 删除配置：
  ```
  <?xml version="1.0" encoding="GBK"?>
  <db version="0.0.1">
      <data>
          <table name="
  AUSFIMSI
  " version="1.0" reparse="false" operation="delete">
          </table>
      </data>
  </db>
  ```

> **说明**
> 该配置数据文件区分中英文，请根据实际使用场景选择对应文件。

## 操作本对象的命令

- [[command/UNC/20.15.2/LOD-CONFIGXML]] · LOD CONFIGXML

## 证据

- 原始手册：`evidence/UNC/20.15.2/CONFIGXML.md`
