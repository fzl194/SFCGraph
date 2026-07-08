---
id: UDG@20.15.2@MMLCommand@LST RELAYIPINFO
type: MMLCommand
name: LST RELAYIPINFO（查询媒体中继IP信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYIPINFO
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继IP地址信息
status: active
---

# LST RELAYIPINFO（查询媒体中继IP信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示媒体中继IP信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYIPNAME | 媒体中继IP地址名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示媒体中继服务IP配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYIPINFO]] · 媒体中继IP信息（RELAYIPINFO）

## 使用实例

显示媒体中继IP地址信息：

```
LST RELAYIPINFO: RELAYIPNAME="test";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
媒体中继IP地址名称  =  test
	   IP业务类型  =  组级IP
	      实例ID  =  0
		IPv4地址  =  192.168.1.1
		IPv6地址  =  ::
	   VPN实例名称 = test_vpn
		配置域名称 = testDomain
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询媒体中继IP信息（LST-RELAYIPINFO）_14777349.md`
