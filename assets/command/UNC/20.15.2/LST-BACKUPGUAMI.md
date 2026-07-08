---
id: UNC@20.15.2@MMLCommand@LST BACKUPGUAMI
type: MMLCommand
name: LST BACKUPGUAMI（查询供备GUAMI信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BACKUPGUAMI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- 备用GUAMI列表管理
status: active
---

# LST BACKUPGUAMI（查询供备GUAMI信息）

## 功能

**适用NF：AMF**

该命令用于查询将本AMF用作备用AMF的GUAMI信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | GUAMI索引 | 可选必选说明：可选参数<br>参数含义：该参数是将本AMF作为备用AMF的GUAMI的配置记录索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BACKUPGUAMI]] · 供备GUAMI信息（BACKUPGUAMI）

## 使用实例

- 查询将本AMF用作备用AMF的“GUAMI索引”为“1”的GUAMI列表，执行如下命令：
  ```
  %%LST BACKUPGUAMI: INDEX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        GUAMI索引  =  1
         备用类型  =  故障
         PLMN索引  =  1
      AMF区域标识  =  01
      AMF集合标识  =  322
  AMF集合内指示符  =  0B
         描述信息  =  for Shanghai AMF11
  (结果个数 = 1)

  ---    END
  ```
- 查询将本AMF用作备用AMF的GUAMI列表，执行如下命令：
  ```
  %%LST BACKUPGUAMI:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        GUAMI索引  =  0
         备用类型  =  故障
         PLMN索引  =  2
      AMF区域标识  =  00
      AMF集合标识  =  001
  AMF集合内指示符  =  01
         描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BACKUPGUAMI.md`
