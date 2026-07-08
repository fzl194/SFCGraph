---
id: UNC@20.15.2@MMLCommand@DSP GREPKTSTAT
type: MMLCommand
name: DSP GREPKTSTAT（查询GRE报文统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GREPKTSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- GRE调测
status: active
---

# DSP GREPKTSTAT（查询GRE报文统计）

## 功能

该命令用于查询GRE报文统计。

## 注意事项

该命令只显示控制面GRE报文计数，不统计转发面报文计数；如果要查询转发面报文计数，可以使用DSP IFCOUNTERS命令查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATTYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定隧道报文统计类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RECV：接收报文统计。<br>- SEND：发送报文统计。<br>默认值：无 |
| TNLNAME | 隧道名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定隧道报文统计接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GREPKTSTAT]] · GRE报文统计（GREPKTSTAT）

## 使用实例

- 查询GRE接收报文统计信息：
  ```
  DSP GREPKTSTAT:STATTYPE=RECV,TNLNAME="tunnel1";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
                  报文总数 = 0
                  非法路径 = 0
                非法IP协议 = 0
              非法乘客协议 = 0
             非法GRE头版本 = 0
                非法Socket = 0
                  非法管道 = 0
              申请内存失败 = 0
                      流控 = 0
                隧道不存在 = 0
                路径不存在 = 0
                  迭代超限 = 0
          识别关键字不匹配 = 0
              非法ICMP报文 = 0
                校验和错误 = 0

          (结果个数 = 1)
          ---    END
  ```
- 查询GRE发送报文统计信息：
  ```
  DSP GREPKTSTAT:STATTYPE=SEND,TNLNAME="tunnel1";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
                  报文总数 = 0
                  非法路径 = 0
                非法IP协议 = 0
              非法乘客协议 = 0
             非法GRE头版本 = 0
                非法Socket = 0
                  非法管道 = 0
              申请内存失败 = 0
                      流控 = 0
                隧道不存在 = 0
                路径不存在 = 0
                  迭代超限 = 0
          识别关键字不匹配 = 0
              非法ICMP报文 = 0
                校验和错误 = 0

          (结果个数 = 1)
          ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GREPKTSTAT.md`
