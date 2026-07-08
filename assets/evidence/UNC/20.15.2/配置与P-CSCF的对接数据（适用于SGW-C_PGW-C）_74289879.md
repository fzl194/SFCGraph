# 配置与P-CSCF的对接数据（适用于SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0174289879__1.3.1)
- [必备事项](#ZH-CN_OPI_0174289879__1.3.2)
- [操作步骤](#ZH-CN_OPI_0174289879__1.3.3)
- [任务示例](#ZH-CN_OPI_0174289879__1.3.4)

## [操作场景](#ZH-CN_OPI_0174289879)

本操作指导介绍了SGW-C/PGW-C与P-CSCF的对接配置，用于部署LTE语音业务。

## [必备事项](#ZH-CN_OPI_0174289879)

前提条件

已完成基础网路部署，如Sv接口，SGs接口对接。

数据

| 命令 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md) | P-CSCF组名（GROUPNAME） | pcg_test1<br>pcg_test2 | 本端规划 | 配置P-CSCF分组信息。 |
| [**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md) | IP地址版本（IPVERSION） | IPV4 | 本端规划 | 配置P-CSCF分组信息。 |
| [**ADD PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/增加P-CSCF地址配置（ADD PCSCFIP）_09651572.md) | P-CSCF组名（GROUPNAME） | pcg_test1<br>pcg_test2 | 已配置数据中获取 | 配置P-CSCF服务器。<br>“P-CSCF组名”<br>从<br>[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)<br>中已配置的数据获取，可通过<br>[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)<br>查询。 |
| [**ADD PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/增加P-CSCF地址配置（ADD PCSCFIP）_09651572.md) | IP地址版本（IPVERSION） | IPV4 | 本端规划 | 配置P-CSCF服务器。<br>“P-CSCF组名”<br>从<br>[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)<br>中已配置的数据获取，可通过<br>[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)<br>查询。 |
| [**ADD PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/增加P-CSCF地址配置（ADD PCSCFIP）_09651572.md) | IPv4地址（PCSCFIPV4） | 192.168.254.251<br>192.168.254.252<br>192.168.254.253<br>192.168.254.254 | 全网规划 | 配置P-CSCF服务器。<br>“P-CSCF组名”<br>从<br>[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)<br>中已配置的数据获取，可通过<br>[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)<br>查询。 |
| [**ADD PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/增加P-CSCF地址配置（ADD PCSCFIP）_09651572.md) | WEIGHT（权重） | 1<br>2<br>3<br>4 | 本端规划 | 配置P-CSCF服务器。<br>“P-CSCF组名”<br>从<br>[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)<br>中已配置的数据获取，可通过<br>[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)<br>查询。 |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | ims | 全网规划 | 配置APN实例。 |
| [**ADD PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/增加APN和P-CSCF组关联关系（ADD PCSCFGRPBNDAPN）_09653091.md) | APN名称（APN） | ims | 已配置数据中获取 | 将指定的主备P-CSCF分组绑定到APN下。<br>- “APN名称”从[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)中已配置的数据获取，可通过[**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)查询。<br>- “主IPv4P-CSCF组”和“备IPv4P-CSCF组”从[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)中已配置的数据获取，可通过[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)查询。 |
| [**ADD PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/增加APN和P-CSCF组关联关系（ADD PCSCFGRPBNDAPN）_09653091.md) | 缺省标记（DEFAULTFLAG） | DEFAULT | 全网规划 | 将指定的主备P-CSCF分组绑定到APN下。<br>- “APN名称”从[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)中已配置的数据获取，可通过[**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)查询。<br>- “主IPv4P-CSCF组”和“备IPv4P-CSCF组”从[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)中已配置的数据获取，可通过[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)查询。 |
| [**ADD PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/增加APN和P-CSCF组关联关系（ADD PCSCFGRPBNDAPN）_09653091.md) | 主IPv4P-CSCF组（MPCSCFGRPIPV4） | pcg_test1 | 已配置数据中获取 | 将指定的主备P-CSCF分组绑定到APN下。<br>- “APN名称”从[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)中已配置的数据获取，可通过[**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)查询。<br>- “主IPv4P-CSCF组”和“备IPv4P-CSCF组”从[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)中已配置的数据获取，可通过[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)查询。 |
| [**ADD PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/增加APN和P-CSCF组关联关系（ADD PCSCFGRPBNDAPN）_09653091.md) | 备IPv4P-CSCF组（SPCSCFGRPIPV4） | pcg_test2 | 已配置数据中获取 | 将指定的主备P-CSCF分组绑定到APN下。<br>- “APN名称”从[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)中已配置的数据获取，可通过[**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)查询。<br>- “主IPv4P-CSCF组”和“备IPv4P-CSCF组”从[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)中已配置的数据获取，可通过[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)查询。 |

## [操作步骤](#ZH-CN_OPI_0174289879)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置P-CSCF分组。
  [**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)
3. 配置P-CSCF服务器。
  [**ADD PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/增加P-CSCF地址配置（ADD PCSCFIP）_09651572.md)
  > **说明**
  > 在配置P-CSCF服务器时，为了更好的实现负荷分担功能，请按照如下原则配置：
  >
  > - 所有服务器都需要配置到主备Group中。
  > - 主备Group的配置顺序不能一致。
  >
  > 比如说有A、B、C、D四台服务器，主备Group都需要配置四台服务器，主Group的顺序为A、B、C、D，备Group的顺序为B、A、D、C。
4. 指定APN实例。
  [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
5. 将指定的主备P-CSCF分组绑定到APN下。
  [**ADD PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/增加APN和P-CSCF组关联关系（ADD PCSCFGRPBNDAPN）_09653091.md)

## [任务示例](#ZH-CN_OPI_0174289879)

任务描述

配置SGW-C/PGW-C与多个P-CSCF建立IP连接。

脚本

进入 “MML命令行-UNC” 窗口。

//配置P-CSCF组名。

```
ADD PCSCFGROUP: GROUPNAME="pcg_test1", IPVERSION=IPV4;
```

```
ADD PCSCFGROUP: GROUPNAME="pcg_test2", IPVERSION=IPV4;
```

//配置P-CSCF分组。

```
ADD PCSCFIP: GROUPNAME="pcg_test1", IPVERSION=IPV4, PCSCFIPV4="192.168.254.251", WEIGHT=1;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test1", IPVERSION=IPV4, PCSCFIPV4="192.168.254.252", WEIGHT=2;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test1", IPVERSION=IPV4, PCSCFIPV4="192.168.254.253", WEIGHT=3;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test1", IPVERSION=IPV4, PCSCFIPV4="192.168.254.254", WEIGHT=4;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test2", IPVERSION=IPV4, PCSCFIPV4="192.168.254.252", WEIGHT=2;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test2", IPVERSION=IPV4, PCSCFIPV4="192.168.254.251", WEIGHT=1;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test2", IPVERSION=IPV4, PCSCFIPV4="192.168.254.254", WEIGHT=4;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test2", IPVERSION=IPV4, PCSCFIPV4="192.168.254.253", WEIGHT=3;
```

//指定APN实例。

```
ADD APN: APN="ims";
```

//将指定的主备P-CSCF分组绑定到APN下。

```
ADD PCSCFGRPBNDAPN: APN="ims", DEFAULTFLAG=DEFAULT, MPCSCFGRPIPV4="pcg_test1", SPCSCFGRPIPV4="pcg_test2";
```
