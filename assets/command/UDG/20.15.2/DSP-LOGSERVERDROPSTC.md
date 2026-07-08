---
id: UDG@20.15.2@MMLCommand@DSP LOGSERVERDROPSTC
type: MMLCommand
name: DSP LOGSERVERDROPSTC（显示日志丢弃统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LOGSERVERDROPSTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 日志管理调测
status: active
---

# DSP LOGSERVERDROPSTC（显示日志丢弃统计信息）

## 功能

该命令用于显示日志丢弃统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LOGSERVERDROPSTC]] · 日志丢弃统计信息（LOGSERVERDROPSTC）

## 使用实例

显示日志丢弃统计信息：

```
DSP LOGSERVERDROPSTC:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
日志ID       丢弃原因       丢弃数量

139591683    日志ID不存在    100  
139591680    日志ID不存在    50   
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示日志丢弃统计信息（DSP-LOGSERVERDROPSTC）_59103338.md`
