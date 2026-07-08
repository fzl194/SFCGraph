---
id: UDG@20.15.2@MMLCommand@DSP OSPFERRORDATA
type: MMLCommand
name: DSP OSPFERRORDATA（查询OSPF进程的错误信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFERRORDATA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF进程的错误信息
status: active
---

# DSP OSPFERRORDATA（查询OSPF进程的错误信息）

## 功能

该命令用于显示OSPF的错误信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFERRORDATA]] · OSPF进程的错误信息（OSPFERRORDATA）

## 使用实例

查看OSPF的错误信息：

```
DSP OSPFERRORDATA:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
                  OSPF进程号  =  1
        相同IP地址数据包计数  =  0
                      错误包  =  0
                  错误版本号  =  0
                  错误校验和  =  0
                  错误区域ID  =  0
              无编号接口丢包  =  0
                错误虚拟连接  =  0
                错误验证类型  =  0
                  错误验证值  =  0
                  数据包过大  =  0
                  数据包过小  =  0
                    传输错误  =  0
                    接口down  =  0
                    未知邻居  =  0
              错误认证序列号  =  0
                  掩码不匹配  =  0
         HelloInterval不匹配  =  0
          DeadInterval不匹配  =  0
                可选项不匹配  =  0
       Hello报文路由器ID冲突  =  0
              虚连接邻居未知  =  0
                NBMA邻居未知  =  0
                      无效源  =  0
                    路由器ID  =  192.168.7.1
                 MTU值不匹配  =  0
              DD可选项不匹配  =  0
          DD报文路由器ID冲突  =  0
           DD报文LSA类型未知  =  0
                    错误确认  =  0
                        DD数  =  0
                       LSR数  =  0
                       LSU数  =  0
                   无效LSA数  =  0
               策略过滤LSA数  =  0
               时限无效LSA数  =  0
              隧道开销值错误  =  0
                    重复确认  =  0
          LSAck包LSA类型未知  =  0
                      空请求  =  0
                    错误请求  =  0
               LSA校验和错误  =  0
            LSU包LSA类型错误  =  0
             新收到自生成LSA  =  1
                 收到超时LSA  =  0
                  9类LSA越界  =  0
                 10类LSA越界  =  0
                 11类LSA越界  =  0
                 越界TLV统计  =  0
          邻居接口类型不匹配  =  0
    邻居状态低不能接收DD报文  =  0
邻居状态低不能接收LS ACK报文  =  0
邻居状态低不能接收LS REQ报文  =  0
邻居状态低不能接收LS UPD报文  =  0
             最小LSA接收间隔  =  2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-OSPFERRORDATA.md`
