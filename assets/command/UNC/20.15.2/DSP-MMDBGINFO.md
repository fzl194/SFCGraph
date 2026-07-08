---
id: UNC@20.15.2@MMLCommand@DSP MMDBGINFO
type: MMLCommand
name: DSP MMDBGINFO（显示MM移动性管理相关的调试信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MMDBGINFO
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 移动性管理调测
- MM模块信息
status: active
---

# DSP MMDBGINFO（显示MM移动性管理相关的调试信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询和移动性管理相关的一些调试信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| MSTATE | 主备状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定节点的主备状态。<br>取值范围：<br>- “MASTER(主用状态)”<br>- “SLAVE(备用状态)”<br>默认值：<br>“MASTER(主用状态)” |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的序号。<br>取值范围：0～20<br>默认值：无 |
| DBGINDEX | 调试索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的类型。<br>取值范围：0～4294967294<br>默认值：无<br>说明：- 1表示查询用于安全调试的参数值。<br>- 2表示查询S1安全统计值。<br>- 3表示查询Gb和Iu安全统计值。<br>- 4表示查询S1 CB与动态SDB组的值。<br>- 5表示查询MM内部流程统计值。<br>- 6表示查询PID间消息（给MM发送的消息统计，以及MM给其他PID发送的消息统计）。 |
| DBGPARA1 | 调试参数1 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA2 | 调试参数2 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA3 | 调试参数3 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA4 | 调试参数4 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA5 | 调试参数5 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA6 | 调试参数6 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA7 | 调试参数7 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA8 | 调试参数8 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA9 | 调试参数9 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| DBGPARA10 | 调试参数10 | 可选必选说明：可选参数<br>参数含义：暂未使用。<br>取值范围：0～255<br>默认值：无 |
| STRPARA1 | 字符串参数1 | 可选必选说明：可选参数<br>参数含义：输入字符串参数。<br>取值范围：1～127位字符串<br>默认值：无 |
| STRPARA2 | 字符串参数2 | 可选必选说明：可选参数<br>参数含义：输入字符串参数。<br>取值范围：1～127位字符串<br>默认值：无 |
| STRPARA3 | 字符串参数3 | 可选必选说明：可选参数<br>参数含义：输入字符串参数。<br>取值范围：1～127位字符串<br>默认值：无 |
| STRPARA4 | 字符串参数4 | 可选必选说明：可选参数<br>参数含义：输入字符串参数。<br>取值范围：1～127位字符串<br>默认值：无 |
| STRPARA5 | 字符串参数5 | 可选必选说明：可选参数<br>参数含义：输入字符串参数。<br>取值范围：1～127位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMDBGINFO]] · MM移动性管理相关的调试信息（MMDBGINFO）

## 使用实例

1. 当调试索引为1时，表示查询用于安全调试的参数值：
  DSP MMDBGINFO: RUNAME="USN_SP_RU_0066", PROCNO=0, DBGINDEX=1;
  ```
  %%DSP MMDBGINFO: RUNAME="USN_SP_RU_0066", PROCNO=0, DBGINDEX=1;%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------
   名称                         值

   ULNASMsg integrity check     1           
   PTMSI Signature check        1           
   NASMsg Cipher And Decipher   1           
   Auth Period For Test         0           
   Auth Check                   1           
   Nas Count Wrap Value         2           
   Max Nas Count                16777215    
   Ms Reachable Timer For Test  0           
  (结果个数 = 8)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示MM移动性管理相关的调试信息(DSP-MMDBGINFO)_26145878.md`
