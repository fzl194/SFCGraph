---
id: UNC@20.15.2@MMLCommand@RTR SFEPKTSTATS
type: MMLCommand
name: RTR SFEPKTSTATS（清除SFE统计信息）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: SFEPKTSTATS
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 统计信息
status: active
---

# RTR SFEPKTSTATS（清除SFE统计信息）

## 功能

该命令用于命令清除指定资源单元上的SFE统计信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATISTTYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待清除的SFE内部统计信息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- fei_packet_count：报文计数。<br>- fei_error_count：错误计数。<br>- fei_event_count：事件计数。<br>默认值：无 |
| STATISTSUBTYPE | 统计子类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATISTTYPE”配置为“fei_packet_count”时为可选参数。<br>参数含义：该参数用于指定待清除的统计信息子类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- fei_sub_discard：被SFE丢弃的报文计数。<br>- fei_sub_tocp：准备上送CP的报文计数。<br>- fei_sub_cache：SFE中的报文缓存计数。<br>- fei_sub_in：入SFE报文计数。<br>- fei_sub_out：出SFE报文计数。<br>默认值：无<br>配置原则：如果不设置该参数，则清除所有类型计数。 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFEPKTSTATS]] · SFE统计信息（SFEPKTSTATS）

## 使用实例

清除指定资源单元的被SFE丢弃的报文计数：

```
RTR SFEPKTSTATS:STATISTTYPE=fei_packet_count,STATISTSUBTYPE=fei_sub_discard,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-SFEPKTSTATS.md`
