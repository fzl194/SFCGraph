---
id: UNC@20.15.2@MMLCommand@SET ADDRESSATTR
type: MMLCommand
name: SET ADDRESSATTR（设置UE IP地址属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ADDRESSATTR
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 全局地址分配属性配置
status: active
---

# SET ADDRESSATTR（设置UE IP地址属性）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置UE IP动态地址分配的全局属性。

## 注意事项

- 该命令执行后立即生效。

- 修改该命令仅对后续接入用户生效。
- 当前版本不支持此命令的RELEASEADDRNUM参数。
- 如果APNAUTHATTR中ACCESSMODE配置为LOC_AUTH或TRANS_NON_AUTH，配置ADDRESSATTR中用户的IPv6地址Interface Identifier生成方式设置为RADIUS就会失效，处理同用户的IPv6地址Interface Identifier生成方式设置为LOCAL，即SMF或UPF分配。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ALLOCPRECEDENCE | IPV6INTERFACEID | RECYCLESSTMR | RELEASEADDRNUM | RELEASETMR | UPFADDRUSAGERPT | CONFLICTSTG | RDSWILDCARD | CONFLICTSWITCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UPF_FIRST | LOCAL | 600 | 512 | 5 | FALSE | DEACBOTH | DISABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALLOCPRECEDENCE | UE地址分配属性 | 可选必选说明：可选参数<br>参数含义：该参数用于配置UE IP动态地址分配全局属性。<br>数据来源：全网规划<br>取值范围：<br>- “SMF_ALLOC（SMF分配）”：UE地址由SMF分配。<br>- “UPF_FIRST（UPF优先）”：UE地址优先由UPF分配，如UPF未分配，则由SMF分配。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：<br>- UE地址期望由SMF，PGW-C，GGSN来分配时，配置选择“SMF_ALLOC（SMF分配）”。<br>- 当UE地址期望由UPF分配时，配置选择“UPF_FIRST（UPF优先）”。当UPF不支持U面分地址时，由SMF分配。 |
| IPV6INTERFACEID | 用户的IPv6地址Interface Identifier生成方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定激活应答消息中用户分配的IPv6地址Interface Identifier从本地生成还是RADIUS下发。<br>数据来源：对端协商<br>取值范围：<br>- “LOCAL（本地）”：通过SMF或UPF生成。<br>- “RADIUS（RADIUS）”：通过AAA服务器生成。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：无 |
| RECYCLESSTMR | 地址子段回收定时器(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置地址子段内的地址都释放后，回收该地址子段的等待时长。当控制面为UE分配地址时，以地址子段为单位划分地址资源。当地址子段内的地址分配完成后，地址分配者再申请新的地址子段；当地址子段内的地址都释放后，且经过本参数指定的时长后都没有再分配出去，系统就要回收该地址子段。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~3600，单位是秒。其中0表示立即回收。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：无 |
| RELEASEADDRNUM | 释放租约内地址数量(个) | 可选必选说明：可选参数<br>参数含义：该参数用于设置当控制面无可用地址资源时，一次性回收当前未分配、但是租约未到期的地址的最大数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~10000，单位是个。其中0表示不回收租约内的地址。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：无 |
| RELEASETMR | 会话激活失败地址释放时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置在会话激活失败时地址延迟释放的时长。如果OCS、PCRF/PCF等周边网元闪断导致用户激活失败，当该场景下控制面已经为用户分配的是租约地址时，这些地址在租约内将无法再被分配出去。通过设置本参数值可避免上述异常场景下大量地址资源的无效占用。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~3600，单位是秒。其中0表示立即回收地址。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：无 |
| UPFADDRUSAGERPT | UPF分配地址使用情况上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否统计并上报UPF分配IP地址使用情况。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：<br>如需统计UPF分配IP地址使用情况，建议在网络规划时打开此开关。 |
| CONFLICTSTG | 地址冲突时去激活策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址冲突场景下的去激活策略。当选择的去激活策略为去激活新用户或者去激活新老用户，且新用户是双栈用户时，该新用户会先进行降栈再尝试接入。<br>数据来源：本端规划<br>取值范围：<br>- DEACOLD（去激活老用户）<br>- DEACNEW（去激活新用户）<br>- DEACBOTH（去激活新老用户）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：<br>当DHCP地址冲突时，SET ADDRESSATTR命令的“CONFLICTSTG”参数是否生效受DWORD1041 BIT4控制。 |
| RDSWILDCARD | AAA未下发地址池通配符的情况下是否开启通配功能 | 可选必选说明：可选参数<br>参数含义：该参数用于控制在AAA未下发地址池通配符的情况下是否开启通配功能。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：关闭地址池通配功能<br>- “ENABLE（使能）”：开启地址池通配功能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：无 |
| CONFLICTSWITCH | 静态地址冲突检查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启静态地址冲突检查，包括UDM签约、AAA服务器分配的静态地址。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（去使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRESSATTR查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADDRESSATTR]] · UE IP地址属性（ADDRESSATTR）

## 使用实例

UE地址默认由UPF分配。如希望由SMF分配UE地址，则可以执行如下命令：

```
SET ADDRESSATTR: ALLOCPRECEDENCE=SMF_ALLOC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-ADDRESSATTR.md`
