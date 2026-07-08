---
id: UNC@20.15.2@MMLCommand@LST NRFIPWHITELST
type: MMLCommand
name: LST NRFIPWHITELST（查询NF IP白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFIPWHITELST
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF IP白名单管理
status: active
---

# LST NRFIPWHITELST（查询NF IP白名单）

## 功能

**适用NF：NRF**

该命令用于查询NF IP白名单中的IP段。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数表示NF IP白名单内的IP段类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPV4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数表示NF客户端IPV4地址，用于查询IP白名单中包含此IPV4地址的IP段。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPV6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数表示NF客户端IPV6地址，用于查询IP白名单中包含此IPV6地址的IP段。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFIPWHITELST]] · NF IP白名单（NRFIPWHITELST）

## 使用实例

查询NF IP白名单地址配置信息，执行如下命令：

```
LST NRFIPWHITELST:;
%%LST NRFIPWHITELST:;%%
RETCODE = 0  操作成功

结果如下
--------
IP类型        IPV4地址起始  IPV4地址结束  IPv6起始地址          IPV6结束地址

IPv4 address  10.1.1.1      10.7.7.7      ::                    ::
IPv4 address  10.5.5.5      10.15.15.15   ::                    ::
IPv6 address  0.0.0.0       0.0.0.0       2001:db8:1:1:1:1:1:1  2001:db8:7:7:7:7:7:7
IPv6 address  0.0.0.0       0.0.0.0       2001:db8:6:6:6:6:6:6  2001:db8:20:20:20:20:20:20
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF-IP白名单（LST-NRFIPWHITELST）_29709830.md`
