---
id: UNC@20.15.2@MMLCommand@LST APNRATECTRL
type: MMLCommand
name: LST APNRATECTRL（查询APN速率控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNRATECTRL
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 速率控制
- APN速率控制
- APN速率控制配置
status: active
---

# LST APNRATECTRL（查询APN速率控制配置）

## 功能

**适用NF：PGW-C**

该命令用于查询APN速率控制配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD APN**](../../../APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令配置生成。 |

## 操作的配置对象

- [APN速率控制配置（APNRATECTRL）](configobject/UNC/20.15.2/APNRATECTRL.md)

## 使用实例

- 查询APN名称为test的APN速率控制配置信息：
  ```
  %%LST APNRATECTRL: APN="test";%%
  RETCODE = 0  操作成功

  结果如下
  --------
              APN  =  test
  APN速率控制开关  =  不使能
     上行时间单位  =  不限制
     最大上行速率  =  0
     下行时间单位  =  不限制
     最大下行速率  =  0
  (结果个数 = 1)

  ---    END
  ```
- 查询所有的APN速率控制配置信息：
  ```
  %%LST APNRATECTRL:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN                   APN速率控制开关  上行时间单位  最大上行速率  下行时间单位  最大下行速率  

  0168apn1.com          不使能           不限制        0             不限制        0             
  0168apn2.com          不使能           不限制        0             不限制        0             
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN速率控制配置（LST-APNRATECTRL）_64343877.md`
