---
id: UNC@20.15.2@MMLCommand@MOD QCIPAGINGINFO
type: MMLCommand
name: MOD QCIPAGINGINFO（修改QCI寻呼策略参数配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: QCIPAGINGINFO
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- QCI寻呼策略参数配置
status: active
---

# MOD QCIPAGINGINFO（修改QCI寻呼策略参数配置）

## 功能

**适用网元：MME**

该命令用于修改QCI（QoS Class Identifier）寻呼策略配置。系统可以通过对特性QCI的寻呼策略参数配置来决定寻呼的等待间隔和次数。

## 注意事项

- 该命令执行后，需要把移动性扩展功能([**SET MMFUNC**](../MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md))配置中的“是否支持QCI寻呼策略选项控制”设置为“YES”才能生效。
- 配置该命令后，针对特定QCI的寻呼策略不再受到EMM配置（[**SET EMM**](../MM协议参数管理/S1模式MM协议参数/设置S1模式MM协议参数(SET EMM)_72225207.md)）的影响。
- 执行该命令可能影响特定QCI业务的寻呼流程效率。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，相关特性的具体信息请参考参数的说明。
- 该命令对于CE MODE B终端（一种eMTC终端）和NB-IoT用户不生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCI | 标准QCI值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要修改的寻呼策略对应的QCI值。<br>数据来源：整网规划<br>取值范围：1～254<br>默认值：无<br>配置原则：1~9级代表着不同类型的业务，按照所使用到的业务，配置相应的映射规则。 10~254级代表自定义类型的业务，其中 65：用于公共安全PTT业务的语音业务。 66：用于普通消费者PTT业务的语音业务。 69：Non-GBR承载，用于公共安全PTT业务的信令。 70：Non-GBR承载，用于公共安全数据业务。 |
| T3413 | T3413（s） | 可选必选说明：可选参数<br>参数含义：该定时器用于控制寻呼间隔的基础时长。该定时器在MME下发Paging Request消息后启动，在收到UE的上行消息后停止，超时后重发Paging Request消息，重发次数由<br>“N3413”<br>参数决定。发送第n次Paging Request后的超时时长计算公式为T3413 + (n-1)*PAGINGDELTA。<br>数据来源：整网规划<br>取值范围：1s～12s<br>默认值：无 |
| N3413 | N3413（times） | 可选必选说明：可选参数<br>参数含义：该参数用于在寻呼流程中，如果MME没有收到UE的响应消息，重复发送寻呼请求消息的次数。超时次数达到配置次数后，寻呼流程失败。<br>数据来源：整网规划<br>取值范围：0times～10times<br>默认值：无 |
| PAGINGDELTA | 重寻呼间隔递增值（s） | 可选必选说明：可选参数<br>参数含义：该参数用于在寻呼流程中，如果MME没有收到UE的响应消息，重复发送Paging Request消息的间隔递增时间值。<br>数据来源：整网规划<br>取值范围：0s～20s<br>默认值：无 |

## 操作的配置对象

- [QCI寻呼策略参数配置（QCIPAGINGINFO）](configobject/UNC/20.15.2/QCIPAGINGINFO.md)

## 使用实例

修改QCI为1的寻呼策略参数配置为T3413为3(s)、N3413为4(times)、重寻呼间隔递增值为5(s)：

MOD QCIPAGINGINFO: QCI=1, T3413=3, N3413=4, PAGINGDELTA=5;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改QCI寻呼策略参数配置(MOD-QCIPAGINGINFO)_72345129.md`
