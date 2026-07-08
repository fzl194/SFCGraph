---
id: UNC@20.15.2@MMLCommand@LST S1ALGPRIORITY
type: MMLCommand
name: LST S1ALGPRIORITY（查询S1模式加密和完整性算法优先级配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1ALGPRIORITY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- S1模式用户安全参数
status: active
---

# LST S1ALGPRIORITY（查询S1模式加密和完整性算法优先级配置信息）

## 功能

**适用网元：MME**

该命令用于查询S1模式加密和完整性算法优先级的信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGTYPE | 算法类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对何种算法设置优先级。<br>数据来源：整网规划<br>取值范围：<br>- “CIPH(LTE加密算法)”<br>- “INTE(LTE完整性算法)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1ALGPRIORITY]] · S1模式加密和完整性算法优先级配置信息（S1ALGPRIORITY）

## 使用实例

1. 查询所有算法优先级：
  LST S1ALGPRIORITY:;
  ```
  %%LST S1ALGPRIORITY:;%%
  RETCODE = 0  操作成功。

  S1加密算法优先级如表
  --------------------
  算法类型       加密算法               算法优先级

  LTE加密算法    采用空加密算法         0         
  LTE加密算法    采用SNOW 3G加密算法    1         
  仍有后续报告输出
  ---    END

  %%LST S1ALGPRIORITY:;%%
  RETCODE = 0  操作成功。

  S1完整性算法优先级如表
  ----------------------
  算法类型         完整性算法               算法优先级

  LTE完整性算法    采用空完整性算法         1         
  LTE完整性算法    采用SNOW 3G完整性算法    0         
  (结果个数 = 4)
  共有2个报告
  ---    END
  ```
2. 根据算法类型为加密算法，查询所有加密算法的优先级：
  LST S1ALGPRIORITY: ALGTYPE=CIPH;
  ```
  %%LST S1ALGPRIORITY: ALGTYPE=CIPH;%%
  RETCODE = 0  操作成功。

  S1加密算法优先级如表
  --------------------
  算法类型       加密算法               算法优先级

  LTE加密算法    采用空加密算法         0         
  LTE加密算法    采用SNOW 3G加密算法    1         
  (结果个数 = 2)
  ---    END
  ```
3. 根据算法类型为完整性算法，查询所有完整性算法优先级：
  LST S1ALGPRIORITY: ALGTYPE=INTE;
  ```
  %%LST S1ALGPRIORITY: ALGTYPE=INTE;%%
  RETCODE = 0  操作成功。

  S1完整性算法优先级如表
  ----------------------
  算法类型         完整性算法               算法优先级

  LTE完整性算法    采用空完整性算法         1         
  LTE完整性算法    采用SNOW 3G完整性算法    0         
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-S1ALGPRIORITY.md`
