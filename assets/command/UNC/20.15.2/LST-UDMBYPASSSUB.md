---
id: UNC@20.15.2@MMLCommand@LST UDMBYPASSSUB
type: MMLCommand
name: LST UDMBYPASSSUB（查询UDM Bypass最小签约数据配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UDMBYPASSSUB
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- UDM故障BYPASS最小签约数据配置管理
status: active
---

# LST UDMBYPASSSUB（查询UDM Bypass最小签约数据配置）

## 功能

**适用NF：AMF**

该命令用于查询UDM Bypass最小签约数据配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置UDM Bypass最小签约数据集的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），UDM Bypass最小签约数据集的匹配优先级从高到低依次为：“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于系统根据指定用户的IMSI前缀进行匹配，从而区分不同的用户群。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UDMBYPASSSUB]] · UDM Bypass最小签约数据配置（UDMBYPASSSUB）

## 使用实例

查询“用户范围”为“本网用户”的UDM Bypass最小签约数据配置，执行如下命令：

```
%%LST UDMBYPASSSUB: SUBRANGE=HOME_USER;%%
RETCODE = 0  操作成功

结果如下
--------
                         用户范围  =  本网用户
                         IMSI前缀  =  NULL
                       UE使用特征  =  0
                     MICO模式标识  =  FALSE
               运营商闭锁分组业务  =  没有配置或者无效配置业务
         是否支持网络切片包含模式  =  FALSE
          是否配置SMF选择签约数据  =  关闭
                  SMF选择签约数据  =  NULL
是否允许漫游场景下进行DNN本地分流  =  FALSE
              DNN是否支持EPS互操作 =  FALSE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UDM-Bypass最小签约数据配置（LST-UDMBYPASSSUB）_32654395.md`
