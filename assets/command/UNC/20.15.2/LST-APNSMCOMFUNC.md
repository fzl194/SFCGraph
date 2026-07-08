---
id: UNC@20.15.2@MMLCommand@LST APNSMCOMFUNC
type: MMLCommand
name: LST APNSMCOMFUNC（查询APN粒度的通用会话拓展功能控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNSMCOMFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话管理拓展功能
- APN级通用会话拓展功能
status: active
---

# LST APNSMCOMFUNC（查询APN粒度的通用会话拓展功能控制）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询APN粒度的通用会话拓展功能控制。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNSMCOMFUNC]] · APN粒度的通用会话拓展功能控制（APNSMCOMFUNC）

## 使用实例

- 显示“APN名称”为“huawei.com”的APN粒度通用会话拓展功能控制：
  ```
  %%LST APNSMCOMFUNC: APN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  --------
              APN名称  =  huawei.com
  在EPS是否先获取策略  =  使能
  (结果个数 = 1)

  ---    END
  ```
- 显示全部APN的通用会话拓展功能控制：
  ```
  %%LST APNSMCOMFUNC:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称  	在EPS是否先获取策略  
  huawei.com  	使能                 
  huawei2.com    	使能          
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNSMCOMFUNC.md`
