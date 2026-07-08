---
id: UDG@20.15.2@MMLCommand@RST DBINSTANCE
type: MMLCommand
name: RST DBINSTANCE（复位CSDB子实例）
nf: UDG
version: 20.15.2
verb: RST
object_keyword: DBINSTANCE
command_category: 动作类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 实例管理
status: active
---

# RST DBINSTANCE（复位CSDB子实例）

## 功能

![](复位CSDB子实例（RST DBINSTANCE）_29626988.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当，子实例所属的集群的数据会被清空，请谨慎使用并联系华为技术支持协助操作。

该命令用于复位指定的子实例。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 子实例标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个子实例，可以通过<br>**[DSP DBINSTANCE](查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～100。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DBINSTANCE]] · 复位CSDB子实例（DBINSTANCE）

## 使用实例

复位标识为 “1” 的子实例：

RST DBINSTANCE: INSTANCEID=1;

```
%%
RST DBINSTANCE: INSTANCEID=1
;%%
RETCODE = 0  Operation succeeded

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/复位CSDB子实例（RST-DBINSTANCE）_29626988.md`
