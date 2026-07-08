---
id: UDG@20.15.2@MMLCommand@LST URR
type: MMLCommand
name: LST URR（查询URR）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: URR
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 使用率上报规则
status: active
---

# LST URR（查询URR）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询使用量上报规则信息。当运营商希望查询使用量上报规则信息时，则执行该命令。

## 注意事项

如果不输入使用量上报规则信息名称，表示查询系统中所有使用量上报规则信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| URRNAME | 使用量上报规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置URR名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/URR]] · URR（URR）

## 使用实例

- 假如运营商需要查询名称为onlineurr的使用量上报规则信息：
  ```
  LST URR: URRNAME="onlineurr";
  ```
  ```

  RETCODE = 0  操作成功。

  使用量上报规则信息：
  --------------------
    使用量上报规则名称  =  onlineurr
               URR标识  =  1000
        使用量上报模式  =  在线计费
      离线计费统计类型  =  流量
      在线计费统计类型  =  免费
    默认时长配额（秒）  =  0
          默认流量配额  =  0
    默认流量配额的单位  =  字节
            配置域名称  =  NULL
                计费组  =  NULL
              业务标识  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询所有的使用量上报规则信息：
  ```
  LST URR:;
  ```
  ```

  RETCODE = 0  操作成功。

  使用量上报规则信息：
  --------------------
  使用量上报规则名称    URR标识    使用量上报模式    离线计费统计类型    在线计费统计类型    默认流量配额    默认流量配额的单位    默认时长配额（秒）    配置域名称    计费组    业务标识

  onlineurr             1000       在线计费          流量                免费                0               字节                  0                     NULL          NULL      NULL
  test1                 1          监控属性值        流量                免费                0               字节                  0                     NULL          NULL      NULL
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-URR.md`
