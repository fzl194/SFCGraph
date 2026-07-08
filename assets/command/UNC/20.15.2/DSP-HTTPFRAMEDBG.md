---
id: UNC@20.15.2@MMLCommand@DSP HTTPFRAMEDBG
type: MMLCommand
name: DSP HTTPFRAMEDBG（显示HTTP调试信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HTTPFRAMEDBG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP平台管理
status: active
---

# DSP HTTPFRAMEDBG（显示HTTP调试信息）

## 功能

该命令用于查询HTTP微服务框架内部运行信息，确认内部模块的运行状态是否正常。

## 注意事项

- 若需执行此命令，请联系华为技术支持。
- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBGSTR | 调试命令 | 可选必选说明：可选参数<br>参数含义：该参数指定具体查询类型的字符串名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPFRAMEDBG]] · HTTP调试信息（HTTPFRAMEDBG）

## 使用实例

- 调试命令参数输入为空时，用于查询该命令支持的服务名。
  ```
  %%DSP HTTPFRAMEDBG:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  HttpCtrlSvc     1034          
  SbiLinkCtrlSvc  1022          
  (结果个数 = 2)
  ```
- 调试命令参数输入为"HttpCtrlSvc extcomm VPN present"时，用于查询HttpCtrlSvc下发的VPN策略。
  ```
  %%DSP HTTPFRAMEDBG: DBGSTR="HttpCtrlSvc extcomm VPN present";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
    名称  =  >
  结果值  =  VPNName:"_public_" UseLb:true
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-HTTPFRAMEDBG.md`
