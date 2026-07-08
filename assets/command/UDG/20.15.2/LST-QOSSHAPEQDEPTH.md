---
id: UDG@20.15.2@MMLCommand@LST QOSSHAPEQDEPTH
type: MMLCommand
name: LST QOSSHAPEQDEPTH（查询Qos Shape缓存队列深度与流量速率的对应关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: QOSSHAPEQDEPTH
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- 整形队列深度
status: active
---

# LST QOSSHAPEQDEPTH（查询Qos Shape缓存队列深度与流量速率的对应关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询shaping速率及队列深度的对应关系表。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATE | Qos Shape速率（千比特/秒） | 可选必选说明：可选参数<br>参数含义：指定shaping的流量速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSSHAPEQDEPTH]] · Qos Shape缓存队列深度与流量速率的对应关系（QOSSHAPEQDEPTH）

## 使用实例

- 查询流量速率为128kbps的缓存队列深度与流量速率的对应关系：
  ```
  LST QOSSHAPEQDEPTH:RATE=128;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  Qos Shape速率（千比特/秒）  =  128
     Shape缓存队列深度（包）  =  32
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的QoS Shape缓存队列深度与流量速率的对应关系：
  ```
  LST QOSSHAPEQDEPTH:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  Qos Shape速率（千比特/秒）    Shape缓存队列深度（包）

  2                             1                      
  128                           32                     
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Qos-Shape缓存队列深度与流量速率的对应关系（LST-QOSSHAPEQDEPTH）_86528799.md`
