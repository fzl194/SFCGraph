---
id: UNC@20.15.2@MMLCommand@SET GBLOCPORTRGE
type: MMLCommand
name: SET GBLOCPORTRGE（设置本端端口号选择范围）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GBLOCPORTRGE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- 本端端点端口号管理
status: active
---

# SET GBLOCPORTRGE（设置本端端口号选择范围）

## 功能

**适用网元：SGSN**

此命令用于设置自动上报NSE的本端端点选择端口号的范围。

当自动配置的NSE分配本端端点时，如果NSEI值在本配置命令配置的端口范围内并且没有被其他NSE（包括知名端口：3386、2123、2152、4784、53、123、3784、3785、4500）占用，则分配端口号为NSEI。否则从本配置命令配置的端口范围内随机选择一个未被占用的端口号（携带不同ip地址的NSE可以使用同一端口）。新分配的端口使用新的范围配置，对已分配的无影响。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。
- 如果不执行此命令，则系统缺省值参见下面参数的系统初始设置值。
- 如果存在端口和预置端口相同的本端端点，且该本端端点的IP地址在Gb地址池中，则设置预置端口失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PORTBGN | 起始端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定起始端口号。<br>数据来源：整网规划<br>取值范围：1024～65535<br>系统初始设置值：1024<br>配置原则：端口号的起始值小于结束值。 |
| PORTEND | 结束端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定结束端口号。<br>数据来源：整网规划<br>取值范围：1024～65535<br>系统初始设置值：10000<br>配置原则：端口号的起始值小于结束值。 |
| BEGINPRECFGPORT | 起始预置端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定动态流程上报的预配置端口，BSC侧配置的对端端口号应该在[BEGINPRECFGPORT，BEGINPRECFGPORT+PRECFGPORTNUM-1]范围内，进行动态流程协商时发送使用。<br>数据来源：整网规划<br>取值范围：1024～65535<br>系统初始设置值：2000 |
| PRECFGPORTNUM | 预置端口数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定动态流程上报的预配置端口个数。<br>数据来源：整网规划<br>取值范围：1～512<br>系统初始设置值：128 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端端口范围的描述信息。<br>数据来源：整网规划<br>取值范围：1～33位字符串<br>系统初始设置值：DEFAULT |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBLOCPORTRGE]] · 本端端口号选择范围（GBLOCPORTRGE）

## 使用实例

设置本端端点的 “起始端口号” 为 “1024” ， “结束端口号 ” 为 “10000” ， “预配置端口号” 为 “2000” ， “描述信息 ” 为 “DEFAULT” ：

SET GBLOCPORTRGE: PORTBGN=1024, PORTEND=10000, BEGINPRECFGPORT=2000, DESC="DEFAULT";

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置本端端口号选择范围(SET-GBLOCPORTRGE)_26146000.md`
