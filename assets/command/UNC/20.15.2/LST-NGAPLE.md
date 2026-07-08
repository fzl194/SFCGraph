---
id: UNC@20.15.2@MMLCommand@LST NGAPLE
type: MMLCommand
name: LST NGAPLE（查询NGAP本端实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGAPLE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP本端实体管理
status: active
---

# LST NGAPLE（查询NGAP本端实体）

## 功能

**适用NF：AMF**

该命令用于查询NGAP本端实体配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGAPLEIDX | NGAP本端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGAP本端实体的索引，该索引作为NGAP本端实体的唯一标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NGAP本端实体（NGAPLE）](configobject/UNC/20.15.2/NGAPLE.md)

## 使用实例

- 查询已经配置的所有NGAP本端实体，执行如下命令：
  ```
  %%LST NGAPLE:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NGAP本端实体索引  SCTP本端实体组索引  NGAP参数索引

  1                 1                   0             
  2                 2                   0             
  (结果个数 = 2)

  ---    END
  ```
- 输入NGAP本端实体标识，查询指定的NGAP本端实体，执行如下命令：
  ```
  %%LST NGAPLE: NGAPLEIDX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    NGAP本端实体索引  =  1
  SCTP本端实体组索引  =  1
        NGAP参数索引  =  0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NGAP本端实体（LST-NGAPLE）_09652502.md`
