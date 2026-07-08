---
id: UNC@20.15.2@MMLCommand@LST DRDCI
type: MMLCommand
name: LST DRDCI（查询DC间通信通道信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DRDCI
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRDCI（查询DC间通信通道信息）

## 功能

该命令用于查询DC间通信通道信息。

## 注意事项

- 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
- 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定容灾组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：<br>可通过<br>[**LST DRGROUPINFO**](查询容灾组信息（LST DRGROUPINFO）_74835153.md)<br>命令获取返回结果中的容灾组标识作为参数输入。 |
| IPVERSION | IP版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于配置容灾控制通道IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4类型地址）<br>- IPV6（IPv6类型地址）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DRDCI]] · DC间通信通道信息（DRDCI）

## 使用实例

查询DC间通信通道信息：

```
%%LST DRDCI: DRGROUPID=1, IPVERSION=IPV4;%%
RETCODE = 0  操作成功

结果如下
--------
           容灾组标识                  =  1
           IP版本号                    =  IPv4类型地址
           本端DC通信IPv4地址          =  172.16.3.4
           对端DC通信IPv4地址          =  172.16.5.6
           VPN实例名称                 =  12345
           数据备份模式                =  主备（冷备）容灾模式，无数据备份
           心跳探测时长                =  10
           心跳重传次数                =  6
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DC间通信通道信息（LST-DRDCI）_23714706.md`
