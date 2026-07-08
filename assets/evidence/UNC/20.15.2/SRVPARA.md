# 查询业务参数配置（LST SRVPARA）

- [命令功能](#ZH-CN_CONCEPT_0251174335__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251174335__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0251174335__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0251174335__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0251174335__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0251174335__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0251174335__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0251174335)

**适用NF：NCG**

用于查询NCG相关参数信息。

#### [注意事项](#ZH-CN_CONCEPT_0251174335)

无。

#### [本地用户权限](#ZH-CN_CONCEPT_0251174335)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0251174335)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251174335)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVPARATYPE | 业务参数类型 | 可选必选说明：必选参数<br>参数含义：用于指定对哪一类业务参数进行修改。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GATRACEMSGPARA：Ga跟踪消息长度。<br>- PASSIVEPARA：PASSIVE模式参数。<br>- ANOTHERNODEDOWNPARA：另一节点发生故障。<br>- CDMPULLMODEPARA：PULL分发模式参数。<br>- GALICCTRLALM：GA License控制告警阈值。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0251174335)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0251174335)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 业务参数类型 | 用于指定对哪一类业务参数进行修改。 |
| Ga跟踪消息长度 | 用于设置Ga跟踪消息并且消息类型是DataTransferRequest时的上报长度控制。 |
| 起始端口 | PULL模式下FTP PASSIVE和PORT模式的起始端口。 |
| 结束端口 | PULL模式下FTP PASSIVE和PORT模式的结束端口。 |
| 业务控制参数 | 软参值的开关状态。 |
| SFTP最大超时次数 | PULL模式下SFTP服务端的ClientAliveCountMax参数。 |
| SFTP服务器端向客户端请求消息的时间间隔 | PULL模式下SFTP服务端的ClientAliveInterval参数。 |
| SFTP CPU最高占比（%） | PULL模式下SFTP服务端的CPU最高占比。 |
| FTP CPU最高占比（%） | PULL模式下FTP服务端的CPU最高占比。 |
| 容量告警百分比（%） | 上报告警<br>[ALM-82015](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82015 License过载_51174210.md)<br>的GA接口系统话务量峰值占License值百分比。 |
| 容量告警恢复百分比（%） | 恢复告警<br>[ALM-82015](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82015 License过载_51174210.md)<br>的GA接口系统话务量峰值占License值百分比。 |
| 告警检测周期（分钟） | 告警<br>[ALM-82015](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82015 License过载_51174210.md)<br>的检测周期。 |
