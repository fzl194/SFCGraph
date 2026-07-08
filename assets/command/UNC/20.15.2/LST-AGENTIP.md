---
id: UNC@20.15.2@MMLCommand@LST AGENTIP
type: MMLCommand
name: LST AGENTIP（查询远端地址池代理IP信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AGENTIP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 代理IP管理
status: active
---

# LST AGENTIP（查询远端地址池代理IP信息）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询远端地址池的代理IP地址。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置代理IP地址的地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“_”、“#”、“$”和“&”等，由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| SECTIONNUM | 地址段号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置代理IP地址的地址段号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63，65535。<br>默认值：无<br>配置原则：<br>当没有配置地址段时，此DHCP服务器分配的地址采用主机路由方式发布。当该参数的取值为65535时，表示该参数无效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AGENTIP]] · 远端地址池代理IP信息（AGENTIP）

## 使用实例

当需要查询远端地址池pool1段号为0的代理IP地址时，使用该命令：

```
%%LST AGENTIP:POOLNAME="pool1",SECTIONNUM=0;%%
RETCODE = 0  操作成功

结果如下
--------
  地址池名称  =  pool1
    地址段号  =  0
  IP地址类型  =  IPV4
IPv4代理地址  =  10.10.110.1
IPv6代理地址  =  ::
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询远端地址池代理IP信息（LST-AGENTIP）_87302920.md`
