---
id: UNC@20.15.2@MMLCommand@LST PCFSELPLCY
type: MMLCommand
name: LST PCFSELPLCY（查询PCF选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCFSELPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- PCF选择策略管理
status: active
---

# LST PCFSELPLCY（查询PCF选择策略）

## 功能

**适用NF：AMF**

该命令用于查询PCF的选择策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用PCF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “USER_GROUP（用户群）”：用户群<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），PCF选择策略的匹配优先级从高到低依次为：“USER_GROUP(用户群)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用PCF策略的用户的IMSI前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>“IMSIPRE”为预留参数，该策略暂未实现。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCFSELPLCY]] · PCF选择策略（PCFSELPLCY）

## 使用实例

查询“用户范围”为“所有用户”的PCF选择策略，执行如下命令：

```
%%LST PCFSELPLCY: SUBRANGE=ALL_USER;%%
RETCODE = 0  操作成功

结果如下
------------------------
             用户范围  =  所有用户
         用户群组标识  =  0
             控制模式  =  白名单
     是否使用目标PLMN  =  是
         是否使用SUPI  =  是
         是否使用GPSI  =  否
     是否使用网络切片  =  否
          是否重选PCF  =  是
    是否支持PCF重定向  =  否
             服务范围  =  NULL
是否携带Serving Scope  =  否
     是否区分跨省漫游  =  否
     区域标识起始位置  =  0
     区域标识终止位置  =  0
             描述信息  =  NULL
			 IMSI前缀  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCFSELPLCY.md`
