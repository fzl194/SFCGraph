---
id: UNC@20.15.2@MMLCommand@SET SCALINGCTRL
type: MMLCommand
name: SET SCALINGCTRL（设置扩缩容业务控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SCALINGCTRL
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 业务调测
- 扩缩容业务控制参数
status: active
---

# SET SCALINGCTRL（设置扩缩容业务控制参数）

## 功能

**适用网元：MME**

设置产品扩缩容时业务控制参数。

## 注意事项

系统暂不支持该命令。

## 权限

manage-ug；system-ug。
G_1，管理员级别命令组；G_2，操作员级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCALEWINDOW | 暂态业务保护时长（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设定扩缩容时保护用户暂态业务的时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～10。<br>系统初始设置值：0<br>说明：当此参数设置为<br>“0”<br>时，表示设定扩缩容时不保护用户暂态业务。 |
| SCTPREBALANCESW | SCTP链路自动均衡开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩容时SCTP链路自动均衡的控制开关。<br>数据来源：本端规划<br>取值范围：<br>- ON(开启)<br>- OFF(关闭)<br>系统初始设置值：ON(开启) |
| GTPREBALANCESW | GTP路径自动均衡开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩容时GTP路径自动均衡的控制开关。<br>数据来源：本端规划<br>取值范围：<br>- ON(开启)<br>- OFF(关闭)<br>系统初始设置值：ON(开启) |

## 操作的配置对象

- [扩缩容业务控制参数（SCALINGCTRL）](configobject/UNC/20.15.2/SCALINGCTRL.md)

## 使用实例

设置 “暂态业务保护时长(秒)” 为 “5” ， “SCTP链路自动均衡开关” 和 “GTP路径自动均衡开关” “ON(开启)” ：

```
SET SCALINGCTRL: SCALEWINDOW = 5,SCTPREBALANCESW = ON,GTPREBALANCESW = ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置扩缩容业务控制参数(SET-SCALINGCTRL)_26305674.md`
