---
id: UDG@20.15.2@MMLCommand@LST FLOWLETPARA
type: MMLCommand
name: LST FLOWLETPARA（查询大流优化参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FLOWLETPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
- SGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 流量转发管理
- 大流检测功能
status: active
---

# LST FLOWLETPARA（查询大流优化参数）

## 功能

**适用NF：PGW-U、UPF、SGW-U**

该命令用于查询大流优化参数。

> **说明**
> 最多可输入1条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [大流优化参数（FLOWLETPARA）](configobject/UDG/20.15.2/FLOWLETPARA.md)

## 使用实例

1. 查询大流优化参数：
  ```
  LST FLOWLETPARA:;
  RETCODE = 0  操作成功
  结果如下：
  ----------
               大流优化功能  =  关闭大流优化
           线程负载更新间隔  =  256
               大流检测速率  =  78000
         大流优化保护报文数  =  64
         大流优化的保护时间  =  10
      启动优化的线程CPU阈值  =  80
  启动优化的线程CPU偏差阈值  =  15
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询大流优化参数(LST-FLOWLETPARA)_82901202.md`
