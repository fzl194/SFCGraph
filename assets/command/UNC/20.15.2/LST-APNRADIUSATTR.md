---
id: UNC@20.15.2@MMLCommand@LST APNRADIUSATTR
type: MMLCommand
name: LST APNRADIUSATTR（查询APN RADIUS配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNRADIUSATTR
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- APN RADIUS域名属性
status: active
---

# LST APNRADIUSATTR（查询APN RADIUS配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询APN的RADIUS相关信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不能以“.”开头，也不能有连续的“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNRADIUSATTR]] · APN RADIUS配置（APNRADIUSATTR）

## 使用实例

- 假设用户要查询所有APN下配置的RADIUS相关信息：
  ```
  %%LST APNRADIUSATTR:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称               增加或剥离域名            域名位置  

  0168apn1.com          不支持增加或剥离域名功能  NULL
  huawei.com            不支持增加或剥离域名功能  NULL
  (结果个数 = 2)

  ---    END
  ```
- 假设用户要查询APN “huawei.com”下配置的RADIUS相关信息：
  ```
  %%LST APNRADIUSATTR: APN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  --------
         APN名称  =  huawei.com
  增加或剥离域名  =  不支持增加或剥离域名功能
        域名位置  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN-RADIUS配置（LST-APNRADIUSATTR）_28567629.md`
