---
id: UNC@20.15.2@MMLCommand@DSP HPATCH
type: MMLCommand
name: DSP HPATCH（查询热补丁信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HPATCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 升级补丁管理
- 热补丁管理
status: active
---

# DSP HPATCH（查询热补丁信息）

## 功能

该命令用于查询指定网元的微服务热补丁信息。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：用于指示系统需要查询哪个网元对应的热补丁信息。<br>取值范围：0~65535<br>默认值：无。<br>配置原则：无。 |
| SHOWALL | 呈现全部 | 可选必选说明：可选参数。<br>参数含义：用于指定是否展示对应网元的全部热补丁进程数据。<br>取值范围：<br>- TRUE(是)：呈现对应网元全部热补丁进程数据。<br>- FALSE(否)：仅呈现整体统计信息及当前存在异常的数据。<br>默认值：FALSE(否)<br>配置原则：无。 |
| PROCESS_TYPE | 进程类型 | 可选必选说明：可选参数。<br>参数含义：用于指定查询对应进程类型的数据。<br>取值范围：长度不超过64的字符串。<br>默认值：无。<br>配置原则：不包含中文以及如下特殊字符：`~!@#$%^&*()+=\|{}':;,[]<>/?！￥…（）—【】‘；：”“’。，、？ |
| CELL_ID | 进程ID | 可选必选说明：可选参数。<br>参数含义：用于指定查询对应进程ID的数据。<br>取值范围：长度不超过128的字符串。<br>默认值：无。<br>配置原则：不包含中文以及如下特殊字符：`~!@#$%^&*()+=\|{}':;,[]<>/?！￥…（）—【】‘；：”“’。，、？ |
| PATCH_STATUS | 补丁状态 | 可选必选说明：可选参数。<br>参数含义：用于查询指定的补丁状态。<br>取值范围：<br>- ALL(全部)<br>- NORMAL(正常)<br>- ABNORMAL(异常)<br>默认值：ALL。<br>配置原则：无。 |

## 操作的配置对象

- [热补丁（HPATCH）](configobject/UNC/20.15.2/HPATCH.md)

## 使用实例

1. 查询热补丁的统计信息：
  ```
  %%DSP HPATCH: MEID=0, SHOWALL=FALSE;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
    网元ID  =  0
  网元版本  =  22.1.RC1.B070
  补丁版本  =  22.1.RC1.2
      总数  =  2
    异常数  =  0
  (结果个数 = 1)

  ---    END
  ```
2. 查询热补丁的全部数据：
  ```
  %%DSP HPATCH: MEID=0, SHOWALL=TRUE, PATCH_STATUS=ALL;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
  网元ID 进程ID                                                                 补丁版本    进程类型             补丁名称              类型  补丁状态  

  0      0CSPCPMServiceDemo0cspcpmservice-0-c67c95b76-hvzxbCELL_CPMServiceDEMO  22.1.RC1.2  CELL_CPMServiceDEMO  cpm_WORKERHP0001.pat  c     Normal    
  0      0CSPCPMServiceDemo0cspcpmservice-0-c67c95b76-k9jwzCELL_CPMServiceDEMO  22.1.RC1.2  CELL_CPMServiceDEMO  cpm_WORKERHP0001.pat  c     Normal    
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询热补丁信息(DSP-HPATCH)_13558792.md`
