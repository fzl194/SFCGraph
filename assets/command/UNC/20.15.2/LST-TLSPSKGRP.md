---
id: UNC@20.15.2@MMLCommand@LST TLSPSKGRP
type: MMLCommand
name: LST TLSPSKGRP（查询预共享密钥组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TLSPSKGRP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS预共享密钥组管理
status: active
---

# LST TLSPSKGRP（查询预共享密钥组）

## 功能

该命令用于查询预共享密钥组信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSKGRPIDX | 预共享密钥组索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TLS预共享密钥组的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TLSPSKGRP]] · 预共享密钥组信息（TLSPSKGRP）

## 使用实例

- 需要查询组索引为1的TLS预共享密钥组信息，可执行如下命令：
  ```
  %%LST TLSPSKGRP: PSKGRPIDX=1;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
            预共享密钥组索引  =  1
                        描述  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 需要查询所有的TLS预共享密钥组信息，可执行如下命令：
  ```
  %%LST TLSPSKGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
            预共享密钥组索引  =  1
                        描述  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询预共享密钥组（LST-TLSPSKGRP）_57229444.md`
