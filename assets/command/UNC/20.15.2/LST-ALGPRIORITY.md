---
id: UNC@20.15.2@MMLCommand@LST ALGPRIORITY
type: MMLCommand
name: LST ALGPRIORITY（查询算法优先级配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALGPRIORITY
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- Iu模式用户安全参数
status: active
---

# LST ALGPRIORITY（查询算法优先级配置信息）

## 功能

**适用网元：SGSN**

该命令用于查询算法的优先级信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGTYPE | 算法类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对何种算法设置优先级。<br>取值范围：<br>- “CIPH(UMTS加密算法)”<br>- “INTE(UMTS完整性算法)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALGPRIORITY]] · 算法优先级配置信息（ALGPRIORITY）

## 使用实例

1. 查询所有算法优先级：
  LST ALGPRIORITY:;
  ```
  %%LST ALGPRIORITY:;%%
  RETCODE = 0  操作成功。

  算法优先级配置表
  ----------------
   算法类型        算法    算法优先级

   UMTS加密算法    UEA1    5         
   UMTS完整性算法  UIA1    0         
   UMTS完整性算法  UIA2    2         
  (结果个数 = 3)

  ---    END
  ```
2. 根据算法类型为加密算法，查询所有加密算法的优先级：
  LST ALGPRIORITY: ALGTYPE=CIPH;
  ```
  %%LST ALGPRIORITY: ALGTYPE=CIPH;%%
  RETCODE = 0  操作成功。

  算法优先级配置表
  ----------------
    算法类型  =  UMTS加密算法
        算法  =  UEA1
  算法优先级  =  5
  (结果个数 = 1)

  ---    END
  ```
3. 根据算法类型为完整性算法，查询所有完整性算法优先级：
  LST ALGPRIORITY: ALGTYPE=INTE;
  ```
  %%LST ALGPRIORITY: ALGTYPE=INTE;%%
  RETCODE = 0  操作成功。

  算法优先级配置表
  ----------------
   算法类型        算法    算法优先级

   UMTS完整性算法  UIA1    0         
   UMTS完整性算法  UIA2    2         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询算法优先级配置信息(LST-ALGPRIORITY)_26145646.md`
