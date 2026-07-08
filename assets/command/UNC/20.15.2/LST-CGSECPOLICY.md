---
id: UNC@20.15.2@MMLCommand@LST CGSECPOLICY
type: MMLCommand
name: LST CGSECPOLICY（查询安全策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CGSECPOLICY
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
- 计费安全管理
status: active
---

# LST CGSECPOLICY（查询安全策略）

## 功能

**适用NF：NCG**

该命令用于查询NCG对外开放的FTP/SFTP服务的安全策略。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [安全策略（CGSECPOLICY）](configobject/UNC/20.15.2/CGSECPOLICY.md)

## 使用实例

查询系统当前的安全策略：

```
LST CGSECPOLICY:;
```

```
RETCODE = 0  操作成功。

结果如下:
---------
      口令复杂度自定义  =  是
          口令最小长度  =  8
            口令字符集  =  至少两种字符集
          历史口令个数  =  2
  口令是否使用字典词汇  =  是
口令是否允许包含用户名  =  是
    账户锁定策略自定义  =  是
      登录失败尝试次数  =  20
账户持续锁定时间(分钟)  =  300
         SSH算法族策略  =  低密算法
               CDR匿名  =  开启
          分发目录只读  =  开启
SFTP服务端密钥交换算法  =  开启
    SFTP客户端密码策略  =  开启
              迭代次数  =  1000 
       MML话单查询匿名  =  开启
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询安全策略（LST-CGSECPOLICY）_51174351.md`
