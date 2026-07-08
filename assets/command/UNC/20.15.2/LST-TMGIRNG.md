---
id: UNC@20.15.2@MMLCommand@LST TMGIRNG
type: MMLCommand
name: LST TMGIRNG（查询TMGI号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TMGIRNG
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- MB-SMF TMGI配置管理
status: active
---

# LST TMGIRNG（查询TMGI号段）

## 功能

**适用NF：SMF**

该命令用来查询TMGI号段。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。仅支持0-9的数字，所有配置下仅支持同一个MCC、MNC组合。<br>默认值：无<br>配置原则：<br>配置时应与基站支持的MCC保持一致。 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。仅支持0-9的数字，所有配置下仅支持同一个MCC、MNC组合。<br>默认值：无<br>配置原则：<br>配置时应与基站支持的MNC保持一致。 |
| MBSIDRNGSTART | MBS Service ID区域起点值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定组播广播服务标识区域起点值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是8。字符串类型，长度为8位。 必须是0x/X开头的十六进制数，仅支持输入0x/X、0-9、a-f/A-F，字母不区分大小写，取值范围0x000000~0xFFFFFF。<br>默认值：无<br>配置原则：<br>MBSIDRNGSTART一定要小于等于MBSIDRNGEND。 |

## 操作的配置对象

- [TMGI号段（TMGIRNG）](configobject/UNC/20.15.2/TMGIRNG.md)

## 使用实例

当需要查询MCC为460，MNC为03，MBSSERVICEIDSTART为0x000001的TMGI号段时，执行如下命令：

```
%%LST TMGIRNG: MCC="460", MNC="03", MBSIDRNGSTART="0x000001";%%
RETCODE = 0  操作成功

结果如下
--------
              移动国家码  =  460
                移动网号  =  03
MBS Service ID区域起点值  =  0x000001
MBS Service ID区域结束值  =  0x000002
              锁定TMGI段  =  不使能
		是否静态TMGI号段  =  FALSE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TMGI号段（LST-TMGIRNG）_77548762.md`
