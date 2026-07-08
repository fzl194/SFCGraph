---
id: UNC@20.15.2@MMLCommand@SET SDRTRANS
type: MMLCommand
name: SET SDRTRANS（设置SDR传输能力）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SDRTRANS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 服务通信管理
- 传输能力控制
status: active
---

# SET SDRTRANS（设置SDR传输能力）

## 功能

![](设置SDR传输能力（SET SDRTRANS）_30310143.assets/notice_3.0-zh-cn_2.png)

该命令是高危命令，操作不当可能会导致业务受损，请谨慎使用并联系华为技术支持协助操作。可靠传输能力与安全传输能力有关联关系，操作前请参考联机帮助。

该命令用于设置SDR传输能力。SDR传输能力包括可靠传输能力和安全传输能力。

## 注意事项

- 该命令执行后立即生效。

- 若要设置安全传输能力为ENABLEALL或NOTSET，可靠传输能力不能为DISABLEALL。
- 若要禁用可靠传输能力，请确认安全传输能力是否处于开启状态；若安全传输能力处于开启状态，请先禁用安全传输能力再禁用可靠传输能力；若只禁用可靠传输能力却开启安全传输能力，则禁用可靠传输能力只对非加密消息生效，对加密消息不生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FLATTYPE | TRANSABILITY | OPT |
| --- | --- | --- |
| BASE | RELIABILITY | NOTSET |
| BASE | SECURITY | DISABLEALL |
| FABRIC | RELIABILITY | DISABLEALL |
| FABRIC | SECURITY | DISABLEALL |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLATTYPE | 通信平面类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR通信平面类型。<br>数据来源：本端规划<br>取值范围：<br>- “BASE（Base）”：Base平面<br>- “FABRIC（Fabric）”：Fabric平面<br>默认值：无。<br>配置原则：无 |
| TRANSABILITY | 传输能力类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR传输能力类型。<br>数据来源：本端规划<br>取值范围：<br>- “RELIABILITY（可靠传输能力）”：可靠传输能力<br>- “SECURITY（安全传输能力）”：安全传输能力<br>默认值：无。<br>配置原则：无 |
| OPT | 选项开关 | 可选必选说明：该参数在"TRANSABILITY"配置为"RELIABILITY"、"SECURITY"时为条件必选参数。<br>参数含义：该参数用于标识SDR传输能力的选项开关。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLEALL（禁用该传输能力）”：禁用所有消息的该传输能力<br>- “ENABLEALL（启用该传输能力）”：启用所有消息的该传输能力<br>- “NOTSET（不设置该传输能力）”：不设置该传输能力<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SDRTRANS]] · SDR传输能力（SDRTRANS）

## 使用实例

- 设置SDR的BASE平面可靠传输能力：
  ```
  %%SET SDRTRANS: FLATTYPE=BASE, TRANSABILITY=RELIABILITY, OPT=NOTSET;%%
  ```
- 开启安全传输能力前，需先确保可靠传输能力不是DISABLEALL状态，如果查询出来的可靠传输能力是DISABLEALL状态，请先将可靠传输能力置为NOTSET或ENABLEALL：
  ```
  %%LST SDRTRANS:;%%
  %%SET SDRTRANS: FLATTYPE=BASE, TRANSABILITY=RELIABILITY, OPT=NOTSET;%%
  %%SET SDRTRANS: FLATTYPE=BASE, TRANSABILITY=SECURITY, OPT=NOTSET;%%
  ```
- 若要禁用所有消息（包括加密消息）的可靠传输能力，需要先禁用安全能力，再禁用可靠能力：
  ```
  %%SET SDRTRANS: FLATTYPE=BASE, TRANSABILITY=SECURITY, OPT=DISABLEALL;%%
  %%SET SDRTRANS: FLATTYPE=BASE, TRANSABILITY=RELIABILITY, OPT=DISABLEALL;%%
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SDR传输能力（SET-SDRTRANS）_30310143.md`
