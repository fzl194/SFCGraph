# 删除单协议推理配置（RMV INSAPROTPARA）

- [命令功能](#ZH-CN_CONCEPT_0000206906564539__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206906564539__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206906564539__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206906564539__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206906564539__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206906564539)

**适用NF：PGW-U、UPF**

删除单协议推理配置。

#### [注意事项](#ZH-CN_CONCEPT_0000206906564539)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206906564539)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206906564539)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示协议组包含的协议的名字。<br>数据来源：本端规划<br>取值范围：1、字符串类型，输入长度范围为1～31; 2、不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置协议前需使用工程命令smctrldsp protocol-list sub-protocol查询三级协议表；使用MML命令DSP CFGTABLEDATA: OMUTYPE=master, DBTYPE=running, QUERYTYPE=table-data, TABLENAME="AISAppProtocol", SERVICEINSTANCE="ACS";查询INSA自定义协议表。 |

#### [使用实例](#ZH-CN_CONCEPT_0000206906564539)

删除http协议的单条协议推理参数设置：

```
RMV INSAPROTPARA:PROTOCOLNAME="http";
```
