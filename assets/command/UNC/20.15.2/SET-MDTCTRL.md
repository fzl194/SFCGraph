---
id: UNC@20.15.2@MMLCommand@SET MDTCTRL
type: MMLCommand
name: SET MDTCTRL（设置MDT控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MDTCTRL
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- MDT管理
status: active
---

# SET MDTCTRL（设置MDT控制参数）

## 功能

**适用网元：MME**

该命令用于设置MDT控制参数。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MDTSW | MDT开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定最小化路测（MDT）功能开关。<br>数据来源：全网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON（打开）”<br>系统初始设置值：<br>“OFF（关闭）”<br>配置原则：当用户需要最小化路测(MDT)功能时，可以通过设置该参数为“ON(打开)”来开启该功能。 |
| MDTCFGPLCY | 是否向新侧MME携带MDT-Configuration | 可选必选说明：条件可选参数<br>参数含义：指定是否向新侧MME携带MDT-Configuration。<br>前提条件：该参数在“MDT开关”设置为“ON(打开)”后生效。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”<br>- “ON（打开）”<br>系统初始设置值：<br>“OFF（关闭）”<br>配置原则：为保证兼容性，当新侧MME支持MDT-Configuration且需要向新侧MME携带MDT-Configuration时，可以通过设置该参数为“ON(打开)”来开启该功能。<br>说明：当前版本不支持此功能。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MDTCTRL]] · MDT控制参数（MDTCTRL）

## 使用实例

设置MDTCTRL参数，MDTSW为ON，MDTCFGPLCY为ON：

SET MDTCTRL: MDTSW=ON, MDTCFGPLCY=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置MDT控制参数(SET-MDTCTRL)_72345435.md`
