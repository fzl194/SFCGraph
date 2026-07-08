---
id: UDG@20.15.2@MMLCommand@UPD COMPSTATUS
type: MMLCommand
name: UPD COMPSTATUS（收集并推送RU的组件状态）
nf: UDG
version: 20.15.2
verb: UPD
object_keyword: COMPSTATUS
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# UPD COMPSTATUS（收集并推送RU的组件状态）

## 功能

![](收集并推送RU的组件状态（UPD COMPSTATUS）_39786878.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令收集并推送所有RU的组件状态时，可能导致CPU使用率瞬时增加，请避免在业务高峰期使用并联系华为技术支持协助操作。

该命令用于收集并推送RU的组件状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令收集并推送所有RU的组件状态时，可能导致CPU使用率瞬时增加。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时收集并推送所有资源的组件状态信息。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/COMPSTATUS]] · 收集并推送RU的组件状态（COMPSTATUS）

## 使用实例

- 收集并推送所有资源的组件状态信息：
  ```
  UPD COMPSTATUS:SERVICEINSTANCE="vnfc"
  ;
  ```
- 收集并推送VNODE_UGW_VNFC_SPU_0064的组件状态信息：
  ```
  UPD COMPSTATUS:RUNAME="VNODE_UGW_VNFC_SPU_0064",SERVICEINSTANCE="vnfc"
  ;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/UPD-COMPSTATUS.md`
