---
id: UNC@20.15.2@MMLCommand@LST SRVPARA
type: MMLCommand
name: LST SRVPARA（查询业务参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVPARA
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 业务参数管理
status: active
---

# LST SRVPARA（查询业务参数配置）

## 功能

**适用NF：NCG**

用于查询NCG相关参数信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVPARATYPE | 业务参数类型 | 可选必选说明：必选参数<br>参数含义：用于指定对哪一类业务参数进行修改。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GATRACEMSGPARA：Ga跟踪消息长度。<br>- PASSIVEPARA：PASSIVE模式参数。<br>- ANOTHERNODEDOWNPARA：另一节点发生故障。<br>- CDMPULLMODEPARA：PULL分发模式参数。<br>- GALICCTRLALM：GA License控制告警阈值。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVPARA]] · 业务参数配置（SRVPARA）

## 使用实例

- 查询业务参数类型为“Ga跟踪消息长度”的业务参数配置：
  ```
  LST SRVPARA: SRVPARATYPE=GATRACEMSGPARA;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下:
  ---------
   业务参数类型  =  Ga跟踪消息长度
  Ga跟踪消息长度  =  LONG
  (结果个数 = 1)
  ---    END
  ```
- 查询业务参数类型为“PASSIVE模式参数”的业务参数配置：
  ```
  LST SRVPARA: SRVPARATYPE=PASSIVEPARA;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下:
  ---------
  业务参数类型  =  PASSIVE模式参数
      起始端口  =  20060
      结束端口  =  20090
  (结果个数 = 1)
  ---    END
  ```
- 查询业务参数类型为“另一节点发生故障”的业务参数配置：
  ```
  LST SRVPARA: SRVPARATYPE=ANOTHERNODEDOWNPARA;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下:
  ---------
  业务参数类型  =  另一节点发生故障
  业务控制参数  =  开启
  (结果个数 = 1)
  ---    END
  ```

- 查询业务参数类型为“PULL分发模式参数”的业务参数配置：
  ```
  LST SRVPARA: SRVPARATYPE=CDMPULLMODEPARA;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下:
  ---------
                            业务参数类型  =  PULL分发模式参数
                        SFTP最大超时次数  =  5
  SFTP服务器端向客户端请求消息的时间间隔  =  60
                   SFTP CPU最高占比（%）  =  100
                    FTP CPU最高占比（%）  =  100
  (结果个数 = 1)
  ---    END
  ```

- 查询业务参数类型为“GA License控制告警阈值”的业务参数配置：
  ```
  LST SRVPARA: SRVPARATYPE=GALICCTRLALM;
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下:
  -------------------------
                       业务参数类型  =  GA License控制告警阈值
                容量告警百分比（%）  =  80
            容量告警恢复百分比（%）  =  70
               告警检测周期（分钟）  =  20
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SRVPARA.md`
