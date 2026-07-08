---
id: UNC@20.15.2@MMLCommand@LST RCENTER
type: MMLCommand
name: LST RCENTER（查询注册中心）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RCENTER
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
- 注册中心管理
status: active
---

# LST RCENTER（查询注册中心）

## 功能

**适用NF：SMSF**

此命令用于查询注册中心配置。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RCX | 注册中心索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定注册中心的索引。<br>数据来源：本端规划<br>取值范围：0~1<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RCENTER]] · 注册中心（RCENTER）

## 使用实例

1. 查询注册中心索引为0的注册中心配置，可以用如下命令：
  LST RCENTER: RCX=0;
  ```
  %%LST 
  RCENTER
  : 
  RCX
  =0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  注册中心索引  =  0
  注册中心名称  =  noname
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RCENTER.md`
