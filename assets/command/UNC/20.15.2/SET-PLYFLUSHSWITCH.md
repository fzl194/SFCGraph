---
id: UNC@20.15.2@MMLCommand@SET PLYFLUSHSWITCH
type: MMLCommand
name: SET PLYFLUSHSWITCH（设置集合类型策略刷新开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PLYFLUSHSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略核查管理
status: active
---

# SET PLYFLUSHSWITCH（设置集合类型策略刷新开关）

## 功能

该命令用于设置集合类型策略刷新开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH | CYCLE |
| --- | --- |
| ON | 1440 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 集合类型策略刷新开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否开启集合类型策略刷新，ON表示开启，OFF表示关闭。<br>数据来源：本端规划<br>取值范围：<br>- ON（打开集合类型策略刷新开关）<br>- OFF（关闭集合类型策略刷新开关）<br>默认值：无。<br>配置原则：<br>当集合类型策略需要刷新时，打开开关。 |
| CYCLE | 集合类型策略刷新周期 (分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于设置集合类型策略刷新周期，单位分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLYFLUSHSWITCH查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLYFLUSHSWITCH]] · 集合类型策略刷新开关状态（PLYFLUSHSWITCH）

## 使用实例

设置集合类型策略刷新开关为开，刷新周期为1440分钟。

```
%%SET PLYFLUSHSWITCH: SWITCH=ON, CYCLE=1440;%%
RETCODE = 0  操作成功

---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PLYFLUSHSWITCH.md`
