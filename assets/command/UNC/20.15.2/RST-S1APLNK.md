---
id: UNC@20.15.2@MMLCommand@RST S1APLNK
type: MMLCommand
name: RST S1APLNK（复位S1AP连接）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: S1APLNK
command_category: 动作类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1AP链路
status: active
---

# RST S1APLNK（复位S1AP连接）

## 功能

**适用网元：MME**

此命令用于复位S1AP连接。

## 注意事项

- 此命令执行后立即生效。
- 执行此命令会导致S1AP链路连接中断，该eNodeB下所有的业务中断，请慎重使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESETTYPE | 复位类型 | 可选必选说明:可选参数<br>参数含义：待复位的S1AP连接的类型。<br>取值范围：<br>- “ALL”：复位该eNodeB下的所有用户的S1AP连接信息。<br>- “PART”：随机选择该eNodeB下一部分用户的S1AP连接信息，进行复位。<br>默认值：<br>“ALL”<br>说明：用户的S1AP连接指的是每个用户在附着、路由更新等流程中建立的S1逻辑连接，当连接释放时，此用户状态就切换到EMM_IDLE态。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：待复位的S1AP连接的eNodeB的移动国家码。<br>取值范围：3位十进制数<br>默认值：无<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**DSP S1APLNK**](显示S1AP连接状态(DSP S1APLNK)_26146252.md)<br>查看当前系统里面已经存在的S1AP连接信息。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：待复位的S1AP连接的eNodeB的移动网号。<br>取值范围：位数为2或3的十进制数字<br>默认值：无<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**DSP S1APLNK**](显示S1AP连接状态(DSP S1APLNK)_26146252.md)<br>查看当前系统里面已经存在的S1AP连接信息。 |
| ENODEBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：待复位的S1AP连接的eNodeB的类型。<br>取值范围：<br>- “HOME_ENB(HOME_ENB)”<br>- “MACRO_ENB(MACRO_ENB)”<br>默认值：无<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**DSP S1APLNK**](显示S1AP连接状态(DSP S1APLNK)_26146252.md)<br>查看当前系统里面已经存在的S1AP连接信息。 |
| ENODEBID | eNodeB标识 | 可选必选说明：必选参数<br>参数含义：待复位的S1AP连接的eNodeB的标识。<br>取值范围：0～268435455<br>默认值：无<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**DSP S1APLNK**](显示S1AP连接状态(DSP S1APLNK)_26146252.md)<br>查看当前系统里面已经存在的S1AP连接信息。 |

## 操作的配置对象

- [S1AP连接（S1APLNK）](configobject/UNC/20.15.2/S1APLNK.md)

## 使用实例

复位移动国家码为308，移动网号为07，id为2的home eNodeB的偶联上的部分用户的s1连接：

RST S1APLNK: RESETTYPE=PART, MCC="308", MNC="07", ENODEBTYPE=HOME_ENB, ENODEBID=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位S1AP连接(RST-S1APLNK)_72225931.md`
