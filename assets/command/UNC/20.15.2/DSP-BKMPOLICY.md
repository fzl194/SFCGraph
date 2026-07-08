---
id: UNC@20.15.2@MMLCommand@DSP BKMPOLICY
type: MMLCommand
name: DSP BKMPOLICY（查询自动备份策略）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BKMPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 备份管理
status: active
---

# DSP BKMPOLICY（查询自动备份策略）

## 功能

通过 **DSP BKMPOLICY** 命令可获取备份服务的自动备份策略。

## 注意事项

是否进行网络备份参数为关时sftp信息为无效，不返回相关参数。

## 参数

无。

## 操作的配置对象

- [自动备份策略（BKMPOLICY）](configobject/UNC/20.15.2/BKMPOLICY.md)

## 使用实例

1. 查询自动备份策略：
  ```
  %%DSP BKMPOLICY:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
                  自动备份开关  =  开
            自动备份周期（天）  =  1
                  自动备份时间  =  03:00
        本地备份包存留数（个）  =  7
            是否支持不安全算法  =  关
          网络备份能力检查开关  =  开
              是否进行网络备份  =  开
  SFTP服务器备份包存留数（个）  =  -1
              SFTP服务器IP地址  =  10.0.0.0
              SFTP服务器端口号  =  22
                    SFTP用户名  =  user
                      SFTP密码  =  *****
                      目标目录  =  /home
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询自动备份策略(DSP-BKMPOLICY)_40700732.md`
