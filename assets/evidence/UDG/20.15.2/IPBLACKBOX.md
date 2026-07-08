# 查询PP4黑匣子信息（DSP IPBLACKBOX）

- [命令功能](#ZH-CN_CONCEPT_0000001600600877__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600600877__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600600877__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600600877__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600600877__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600600877__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600600877)

该命令用于查询PP4黑匣子信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600600877)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600600877)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600600877)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 黑匣子类型 | 可选必选说明：必选参数<br>参数含义：该参数指定查询的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DROPPED_PING_PKT：丢弃ping报文。<br>- DROPPED_ICMP_PKT：丢弃ICMP报文。<br>- LSM_SMOOTH：本地会话库平滑信息。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600600877)

- 查询PP4黑匣子丢弃ping报文信息：
  ```
  DSP IPBLACKBOX: TYPE=DROPPED_PING_PKT;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果数据
          component pid:  0x00660012  component cid:  0x80660019
          (结果个数 = 1)
          ---    END
  ```
- 查询PP4黑匣子丢弃ICMP报文信息：
  ```
  DSP IPBLACKBOX: TYPE=DROPPED_ICMP_PKT;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果数据
          component pid:  0x00660012  component cid:  0x80660019
          (结果个数 = 1)
          ---    END
  ```
- 查询PP4黑匣子lsmlib平滑信息：
  ```
  DSP IPBLACKBOX: TYPE=LSM_SMOOTH;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果数据
          component pid:  0x00660012  component cid:  0x80660019

          2017-4-27 17:13:59:475-00:00  Add sock pidnode (0x650005) ok
          2017-4-27 17:13:59:475-00:00  add sock in local 0
          2017-4-27 17:13:59:475-00:00  Add sock pidnode (0x650009) ok
          2017-4-27 17:13:59:475-00:00  add sock in local 0
          2017-4-27 17:13:59:475-00:00  Add sock pidnode (0x650018) ok
          2017-4-27 17:13:59:475-00:00  add sock in local 0
          2017-4-27 17:13:59:475-00:00  Add sock pidnode (0x650020) ok
          2017-4-27 17:13:59:475-00:00  add sock in local 0
          2017-4-27 17:13:59:475-00:00  Add sock pidnode (0x650030) ok
          2017-4-27 17:13:59:475-00:00  add sock in local 0
          2017-4-27 17:13:59:477-00:00  local fsm start work
          2017-4-27 17:13:59:477-00:00  build smooth list
          2017-4-27 17:13:59:477-00:00  add sock(0x650005) to list
          2017-4-27 17:13:59:477-00:00  add sock(0x650009) to list
          2017-4-27 17:13:59:477-00:00  add sock(0x650018) to list
          2017-4-27 17:13:59:477-00:00  add sock(0x650020) to list
          2017-4-27 17:13:59:477-00:00  add sock(0x650030) to list
          2017-4-27 17:14:0:171-00:00  sock(0x650005) state(0)
          2017-4-27 17:14:0:171-00:00  Send smooth request 0x650005
          2017-4-27 17:14:0:171-00:00  sock(0x650009) state(0)
          2017-4-27 17:14:0:171-00:00  Send smooth request 0x650009
          2017-4-27 17:14:0:171-00:00  sock(0x650020) state(0)
          2017-4-27 17:14:0:171-00:00  Send smooth request 0x650020
          2017-4-27 17:14:0:171-00:00  sock(0x650030) state(1)
          2017-4-27 17:14:0:171-00:00  sock(0x650018) state(0)
          2017-4-27 17:14:0:171-00:00  Send smooth request 0x650018
          2017-4-27 17:14:0:171-00:00  fes state(0)
          2017-4-27 17:14:0:172-00:00  Sock(0x650009) query service
          2017-4-27 17:14:0:172-00:00  recv sock(0x650009) smooth begin on 1
          2017-4-27 17:14:0:173-00:00  recv sock(0x650009) smooth end(1) on 2
          2017-4-27 17:14:0:173-00:00  sock(0x650009) smooth over in local 1
          2017-4-27 17:14:0:175-00:00  recv fes notify of service, ucState = 0
          2017-4-27 17:14:0:179-00:00  sock(0x650030) state(0)
          2017-4-27 17:14:0:179-00:00  Send smooth request 0x650030
          2017-4-27 17:14:0:184-00:00  recv fes subbsribe in 1
          2017-4-27 17:14:0:184-00:00  recv fes subbsribe in 1
          2017-4-27 17:14:0:184-00:00  recv fes subbsribe in 1
          2017-4-27 17:14:0:275-00:00  Sock(0x650005) query service
          2017-4-27 17:14:0:275-00:00  Sock(0x650020) query service
          2017-4-27 17:14:0:276-00:00  Sock(0x650018) query service
          2017-4-27 17:14:0:283-00:00  Sock(0x650030) query service
          2017-4-27 17:14:0:470-00:00  Sock(0x650020) query service
          2017-4-27 17:14:0:470-00:00  Sock(0x650030) query service
          2017-4-27 17:14:0:807-00:00  Sock(0x650018) query service
          2017-4-27 17:14:1:183-00:00  Sock(0x650009) query service
          2017-4-27 17:14:1:482-00:00  Send smooth request 0x650005
          2017-4-27 17:14:1:482-00:00  Send smooth request 0x650020
          2017-4-27 17:14:1:482-00:00  Send smooth request 0x650018
          2017-4-27 17:14:1:482-00:00  Send smooth request 0x650030
          2017-4-27 17:14:1:482-00:00  recv sock(0x650020) smooth begin on 1
          2017-4-27 17:14:1:483-00:00  recv sock(0x650005) smooth begin on 1
          2017-4-27 17:14:1:483-00:00  recv sock(0x650020) smooth end(1) on 2
          2017-4-27 17:14:1:483-00:00  sock(0x650020) smooth over in local 1
          2017-4-27 17:14:1:483-00:00  recv sock(0x650005) smooth end(1) on 2
          2017-4-27 17:14:1:483-00:00  sock(0x650005) smooth over in local 1
          2017-4-27 17:14:1:483-00:00  recv sock(0x650030) smooth begin on 1
          2017-4-27 17:14:1:483-00:00  recv sock(0x650018) smooth begin on 1
          2017-4-27 17:14:1:483-00:00  recv sock(0x650030) smooth end(1) on 2
          2017-4-27 17:14:1:483-00:00  sock(0x650030) smooth over in local 1
          2017-4-27 17:14:1:483-00:00  recv sock(0x650018) smooth end(1) on 2
          2017-4-27 17:14:1:483-00:00  sock(0x650018) smooth over in local 1
          2017-4-27 17:14:1:483-00:00  all sock smooth over, fsm into SMOOTHB
          2017-4-27 17:14:1:602-00:00  Sock(0x650005) query service
          2017-4-27 17:14:2:468-00:00  Sock(0x650020) query service
          2017-4-27 17:14:2:468-00:00  Sock(0x650030) query service
          2017-4-27 17:14:2:482-00:00  recv fes smooth begin ack in 2
          2017-4-27 17:14:2:482-00:00  recv fes smooth begin ack in 2
          2017-4-27 17:14:2:482-00:00  recv ipv6 pmtu smooth begin ack in 2
          2017-4-27 17:14:2:482-00:00  recv fes smooth end ack in 4
          2017-4-27 17:14:2:482-00:00  recv fes smooth end ack in 4
          2017-4-27 17:14:2:482-00:00  recv fes smooth end ack in 4
          2017-4-27 17:14:2:482-00:00  fes smooth over in local 2
          2017-4-27 17:14:2:482-00:00  fes smooth over, fsm into RUNNING
          2017-4-27 17:14:2:811-00:00  Sock(0x650018) query service
          2017-4-27 17:14:2:811-00:00  Notify sock(0x650018) in service
          2017-4-27 17:14:3:183-00:00  Sock(0x650009) query service
          2017-4-27 17:14:3:183-00:00  Notify sock(0x650009) in service
          2017-4-27 17:14:3:607-00:00  Sock(0x650005) query service
          2017-4-27 17:14:3:607-00:00  Notify sock(0x650005) in service
          2017-4-27 17:14:4:469-00:00  Sock(0x650030) query service
          2017-4-27 17:14:4:469-00:00  Notify sock(0x650030) in service
          2017-4-27 17:14:4:479-00:00  Sock(0x650020) query service
          2017-4-27 17:14:4:479-00:00  Notify sock(0x650020) in service

          (结果个数 = 1)
          ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600600877)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 查询结果数据 | 用来显示IP黑匣子的查询结果数据。 |
