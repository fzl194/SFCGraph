---
id: UNC@20.15.2@MMLCommand@LST UEUSGTYPEGP
type: MMLCommand
name: LST UEUSGTYPEGP（查询UE USAGE TYPE群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UEUSGTYPEGP
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- UE USAGE TYPE群组管理
status: active
---

# LST UEUSGTYPEGP（查询UE USAGE TYPE群组）

## 功能

**适用网元：MME**

该命令用于查询UE USAGE TYPE群组记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0～1023<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UEUSGTYPEGP]] · UE USAGE TYPE群组（UEUSGTYPEGP）

## 使用实例

1. 不输入参数，查询UE USAGE TYPE群组：
  LST UEUSGTYPEGP:;
  ```
  %%LST UEUSGTYPEGP: UEUSGTYPEGPID=0;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
  UE USAGE TYPE群组标识  =  0
                   描述  =  eMtc
  (结果个数 = 1)

  ---    END
  ```
2. 查询“UEUSGTYPEGPID”为“0”的配置：
  LST UEUSGTYPEGP: UEUSGTYPEGPID=0;
  ```
  %%LST UEUSGTYPEGP: UEUSGTYPEGPID=0;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
  UE USAGE TYPE群组标识  =  0
                   描述  =  eMtc
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UE-USAGE-TYPE群组(LST-UEUSGTYPEGP)_26145822.md`
