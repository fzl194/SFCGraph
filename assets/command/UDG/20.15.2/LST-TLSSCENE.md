---
id: UDG@20.15.2@MMLCommand@LST TLSSCENE
type: MMLCommand
name: LST TLSSCENE（查询TLS证书场景）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TLSSCENE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS证书场景管理
status: active
---

# LST TLSSCENE（查询TLS证书场景）

## 功能

该命令用于查询TLS证书场景配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定证书场景的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~254。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TLSSCENE]] · TLS证书场景（TLSSCENE）

## 使用实例

- 若运营商想查询索引为1的TLS证书场景配置信息，可以用如下命令；
  ```
  %%LST TLSSCENE: INDEX=1;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                 索引  =  1
     证书使用场景名称  =  1
             场景类型  =  CA Certificate Scenario Type
     证书使用场景描述  =  CA
     是否验证本端证书  =  NULL
       本端IP校验开关  =  关闭校验本端证书
  (结果个数 = 1)

  ---    END
  ```
- 若运营商想查询所有的TLS证书场景配置信息，可以用如下命令；
  ```
  %%LST TLSSCENE:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                 索引  =  1
     证书使用场景名称  =  CA
             场景类型  =  CA scene type
     证书使用场景描述  =  CA
     是否验证本端证书  =  NULL
       本端IP校验开关  =  关闭校验本端证书
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TLSSCENE.md`
