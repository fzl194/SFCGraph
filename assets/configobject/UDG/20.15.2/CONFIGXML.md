---
id: UDG@20.15.2@ConfigObject@CONFIGXML
type: ConfigObject
name: CONFIGXML（XML文件配置到数据库）
nf: UDG
version: 20.15.2
object_name: CONFIGXML
object_kind: action
status: active
---

# CONFIGXML（XML文件配置到数据库）

## 说明

![](加载XML文件配置到数据库(LOD CONFIGXML)_49621485.assets/notice_3.0-zh-cn.png)

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

> **说明**
> - 待加载的XML文件必须已上传至OM Portal上“ 系统 > 文件传输 > 原子配置服务 ”下。
> - 请联系华为技术支持人员提供XML，请勿手工修改XML文件格式。
> - 导入的文件格式为“.xml”，单个XML文件大小不能超过100M，写入的配置数据不能超过300000条。
> - 导入的文件格式为“.zip”，压缩包中的文件个数不能超过50个；单个XML文件大小不能超过100M，写入的配置数据不能超过300000条。
> - ZIP包解压后，系统“vrpv8/home”目录磁盘剩余空间至少为100M。
> - 由于XML文件中包含大量配置，加载耗时较长，命令执行过程中会显示当前执行的进度。
> - 当加载ZIP包中的多个XML文件时，如果CPU占用率飙升到阈值以上，系统会暂停加载，并且每隔5秒检查一次CPU占用率，直至CPU占用率下降至阈值以下再启动加载。如果5分钟后CPU占用率仍然在阈值以上，则系统返回加载失败。
> - 加载XML文件会导致CPU占用率飙升，因此当系统CPU占用率超过阈值时，系统可能会拒绝加载，以免CPU进一步飙升，导致系统故障。
> - 加载XML文件前，检查是否存在“ALM-136978434 向远端下发配置执行失败”、“ALM-136978435 与远端配置同步失败”告警。若存在，先参考告警帮助使用**SYN ACSPEERCFG**恢复告警，再执行**LOD CONFIGXML**。
> - 加载XML文件期间，可能无法执行MML命令。
> - 如果XML文件中的配置数据和系统中已有的配置数据冲突，XML文件中冲突的配置数据会加载失败 。
> - 加载XML文件会触发OMSVC进程重启。当系统数据量大时，若OMSVC进程在60秒内没有重启成功或者连续三次重启失败，会上报“ALM-221257751 进程故障”告警，当进程故障恢复时，告警恢复。
> - 加载XML文件完成后，必须执行**SYN ACSPEERCFG**命令，“同步范围”可选择所有或者指定订阅相关业务的微服务，且“同步方式”需要使用“full(全量同步)”，将新导入的数据同步到微服务侧。
> - 加载XML文件完成后，执行**SYN ACSPEERCFG**命令之前，不能执行配置变更相关命令。
> - 加载XML文件完成后，需要查看设备上是否有“ALM-221257751 进程故障”告警，如果有等告警恢复后才可执行**SYN ACSPEERCFG**。或者执行**DSP PROCESSINFO**，“服务实例”填写ACS，“进程类型”填写OMSVC，查询OMSVC进程状态是否为NORMAL，如果不是等待状态恢复为NORMAL才可执行**SYN ACSPEERCFG**。
> - 加载XML文件过程中，依赖的服务故障使命令执行中断，请业务恢复后，重新执行该命令。

## 操作本对象的命令

- [[command/UDG/20.15.2/LOD-CONFIGXML]] · LOD CONFIGXML

## 证据

- 原始手册：`evidence/UDG/20.15.2/CONFIGXML.md`
