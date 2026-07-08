---
id: UDG@20.15.2@MMLCommand@LST RELAYIPSECTION
type: MMLCommand
name: LST RELAYIPSECTION（查询媒体中继IP段）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYIPSECTION
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继回源IP段配置
status: active
---

# LST RELAYIPSECTION（查询媒体中继IP段）

## 功能

**适用NF：UPF**

该命令用于查询媒体中继IP段。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | IP池名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定媒体中继IP段对应的IP池名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：IP池名与IP段ID不能与已有媒体中继IP段冲突。 |
| SECTIONID | IP段ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定媒体中继IP段ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~4294967295。<br>默认值：无<br>配置原则：IP池名与IP段ID不能与已有媒体中继IP段冲突。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYIPSECTION]] · 媒体中继IP段（RELAYIPSECTION）

## 使用实例

假设需要查询媒体中继IP段，则命令如下：

```
LST RELAYIPSECTION:;
```

```

RETCODE = 0  操作成功

结果如下
--------
      IP池名  =  pool_relay
   业务实例ID = 1
      IP段ID  =  1
      IP版本  =  IPV4
    IPv4地址  =  10.2.3.4
IPv4掩码长度  =  30
    IPv6地址  =  ::
IPV6掩码长度  =  0
    是否锁定  =  未锁定
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYIPSECTION.md`
