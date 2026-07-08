---
id: UNC@20.15.2@MMLCommand@LST SGSRLKS
type: MMLCommand
name: LST SGSRLKS（查询SGS服务端链路集）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSRLKS
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SGS服务端链路集
status: active
---

# LST SGSRLKS（查询SGS服务端链路集）

## 功能

**适用NF：SMSF**

此命令用于查询SGS服务端链路集配置。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路集的索引。<br>数据来源：本端规划<br>取值范围：0~2000<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSRLKS]] · SGS服务端链路集（SGSRLKS）

## 使用实例

1. 查询关联索引为0的注册中心链路集配置，可以用如下命令：
  LST SGSRLKS: LSX=0;
  ```
  %%LST SGSRLKS: LSX=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  链路集索引  =  0
     MME索引  =  0
    链路集名  =  noname
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGSRLKS.md`
