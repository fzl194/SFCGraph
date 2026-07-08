---
id: UDG@20.15.2@MMLCommand@DSP TRUNKMEMBER
type: MMLCommand
name: DSP TRUNKMEMBER（显示Trunk成员接口信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TRUNKMEMBER
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- Trunk成员接口配置
status: active
---

# DSP TRUNKMEMBER（显示Trunk成员接口信息）

## 功能

该命令用于显示Trunk成员接口状态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRUNKIFNAME | Trunk接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置Trunk接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TRUNKMEMBER]] · Trunk成员接口（TRUNKMEMBER）

## 使用实例

显示Eth-Trunk1的成员接口信息：

```
DSP TRUNKMEMBER:TRUNKIFNAME="Eth-Trunk1";
```

```

RETCODE = 0  操作成功

结果如下
--------
Trunk接口名    成员接口名        选中状态    成员状态

Eth-Trunk1     Ethernet64/0/3    接口备选    接口up
Eth-Trunk1     Ethernet64/0/4    接口选中    接口down
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示Trunk成员接口信息（DSP-TRUNKMEMBER）_50121638.md`
