---
id: UDG@20.15.2@MMLCommand@DSP SYNCFILESTATUS
type: MMLCommand
name: DSP SYNCFILESTATUS（查询对账文件状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SYNCFILESTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 对账管理
status: active
---

# DSP SYNCFILESTATUS（查询对账文件状态）

## 功能

该命令用于查询ACS服务中的对账文件的生成状态。

> **说明**
> 如果当前系统存在配置变更，与该配置变更相关的对账文件不在结果报文中体现。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| STATUS | 对账文件状态 | 可选必选说明：可选<br>参数含义：用于指示系统按照哪种状态查询对账文件；若不输入，则表示查询所有状态的对账文件。<br>取值范围：枚举类型<br>- all(正在生成和生成结束的文件)：正在生成和生成结束的所有文件，仅作为输入参数的参数值。<br>- generating(正在生成)：文件正在生成。<br>- generated(生成结束)：文件生成结束。<br>默认值：all(正在生成和生成结束的文件) |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SYNCFILESTATUS]] · 对账文件状态（SYNCFILESTATUS）

## 使用实例

- 查询所有状态的对账文件：
  ```
  %%DSP SYNCFILESTATUS: STATUS=all;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  标识号  对账文件名称                  对账文件状态              对账文件生成进度  

  1007.1  DIAM_FLXRT_MGMT_7b629dd3.zip  正在生成和生成结束的文件  100%              
  1007.1  LOG_c2ae5b4f.zip              正在生成和生成结束的文件  100%              
  1007.1  MMCS_194e5de7.zip             正在生成和生成结束的文件  100%              
  1007.1  TimeSirp_64fade63.zip         正在生成和生成结束的文件  100%              
  1007.2  vfabric_f90897b1.zip          正在生成和生成结束的文件  100%              
  1069.1  DIAM_FLXRT_MGMT_49d1b862.zip  正在生成和生成结束的文件  100%              
  1069.1  testxml_312a6aa6.xml          正在生成和生成结束的文件  100%              
  (结果个数 = 7)

  ---    END
  ```

- 查询正在生成的对账文件：
  ```
  %%DSP SYNCFILESTATUS: STATUS=generating;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  标识号  对账文件名称             对账文件状态   对账文件生成进度

  1000.1  test1_d0221b2d.xml       正在生成       90%
  1006.1  test1_4d67aaf3.xml       正在生成       80%
  (结果个数 = 2)

  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SYNCFILESTATUS.md`
