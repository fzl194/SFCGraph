---
id: UNC@20.15.2@MMLCommand@RST SIGBVC
type: MMLCommand
name: RST SIGBVC（复位SigBvc）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: SIGBVC
command_category: 动作类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- 信令实体管理
status: active
---

# RST SIGBVC（复位SigBvc）

## 功能

![](复位SigBvc(RST SIGBVC)_26305840.assets/notice_3.0-zh-cn_2.png)

复位SIG信令实体将导致所有与该SIG信令实体相关的PTP实体被复位，所有相关小区的业务暂时中断。

**适用网元：SGSN**

该命令用于复位SigBvc信令实体，当系统发生影响信令实体功能的故障恢复时，可执行此命令，使BSS和SGSN两端同步初始化信令实体的相关上下文。SigBvc对应了一个NSE。BSS和SGSN中的网络业务实体提供了Gb接口运行需要的网络管理功能，网络业务实体在3GPP TS 48.016中详细描述。

## 注意事项

操作该命令，位于该SigBvc信令实体下的所有小区全部丢失，必须由PCU侧重新发起小区创建流程才能恢复小区信息，SGSN侧与相关小区的所有信息全部丢失。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SIGBVC]] · 复位SigBvc（SIGBVC）

## 使用实例

复位NSEI为10的信令实体：

RST SIGBVC: NSEI=10;

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位SigBvc(RST-SIGBVC)_26305840.md`
